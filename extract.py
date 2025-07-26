
import requests


# Базовый URL
base_url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 20,
        "page": 1,
        "sparkline": False
    }

def get_info():
    response = requests.get(base_url, params = params)
    coins = response.json()
    return coins