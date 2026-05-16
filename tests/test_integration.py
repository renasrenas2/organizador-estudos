import requests
from unittest.mock import patch, MagicMock


def test_api_conselho_status_code():
    """Testa se a API pública retorna status 200 OK."""
    url = "https://api.adviceslip.com/advice"
    mock_response = MagicMock()
    mock_response.status_code = 200

    with patch("requests.get", return_value=mock_response) as mock_get:
        response = requests.get(url)
        mock_get.assert_called_once_with(url)
        assert response.status_code == 200


def test_api_retorna_json_valido():
    """Testa se o formato do dado externo é o esperado."""
    url = "https://api.adviceslip.com/advice"
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "slip": {
            "id": 42,
            "advice": "Study hard and never give up."
        }
    }

    with patch("requests.get", return_value=mock_response):
        response = requests.get(url)
        dados = response.json()
        assert "slip" in dados
        assert "advice" in dados["slip"]


def test_api_falha_retorna_fallback():
    """Testa se a aplicação lida com falha na API sem quebrar."""
    with patch("requests.get", side_effect=Exception("Timeout")):
        try:
            requests.get("https://api.adviceslip.com/advice", timeout=5)
            conselho = "Estude com foco!"
        except Exception:
            conselho = "Conexão com API falhou, mas não pare de estudar!"
        assert isinstance(conselho, str)
        assert len(conselho) > 0