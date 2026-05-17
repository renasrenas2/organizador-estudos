import pytest
from unittest.mock import patch, MagicMock
from src.clima import obter_clima, mensagem_clima


def test_obter_clima_retorna_dados_corretos():
    """Testa se a função obter_clima retorna os campos esperados."""
    mock_resposta = MagicMock()
    mock_resposta.json.return_value = {
        "current_weather": {
            "temperature": 25.0,
            "windspeed": 10.0,
            "weathercode": 0
        }
    }

    with patch("src.clima.requests.get", return_value=mock_resposta):
        dados = obter_clima()

    assert "temperatura" in dados
    assert "velocidade_vento" in dados
    assert "codigo_clima" in dados
    assert dados["temperatura"] == 25.0


def test_mensagem_clima_retorna_string():
    """Testa se mensagem_clima retorna uma string com a temperatura."""
    mock_resposta = MagicMock()
    mock_resposta.json.return_value = {
        "current_weather": {
            "temperature": 28.0,
            "windspeed": 5.0,
            "weathercode": 1
        }
    }

    with patch("src.clima.requests.get", return_value=mock_resposta):
        msg = mensagem_clima()

    assert isinstance(msg, str)
    assert "28.0" in msg


def test_mensagem_clima_falha_graciosamente():
    """Testa se mensagem_clima lida bem com erro de conexão."""
    with patch("src.clima.requests.get", side_effect=Exception("sem internet")):
        msg = mensagem_clima()

    assert "⚠️" in msg