import requests

def test_api_conselho_status_code():
    # Testa se a API pública está online e respondendo 200 OK
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)
    assert response.status_code == 200

def test_api_retorna_json_valido():
    # Testa se o formato do dado externo é o esperado
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)
    dados = response.json()
    assert "slip" in dados
    assert "advice" in dados["slip"]    