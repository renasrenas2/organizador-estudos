import requests

LATITUDE = -15.7801  # Brasília
LONGITUDE = -47.9292


def obter_clima():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={LATITUDE}&longitude={LONGITUDE}"
        "&current_weather=true"
    )
    resposta = requests.get(url, timeout=5)
    resposta.raise_for_status()
    dados = resposta.json()
    clima = dados["current_weather"]
    return {
        "temperatura": clima["temperature"],
        "velocidade_vento": clima["windspeed"],
        "codigo_clima": clima["weathercode"],
    }


def mensagem_clima():
    try:
        dados = obter_clima()
        temp = dados["temperatura"]
        return f"🌤️ Clima agora: {temp}°C — Bom momento para estudar!"
    except Exception:
        return "⚠️ Não foi possível obter o clima agora."