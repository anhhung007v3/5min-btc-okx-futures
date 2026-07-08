import os
import requests
from dotenv import load_dotenv

load_dotenv()


class OKXClient:
    def __init__(self):
        self.base_url = "https://www.okx.com"

    def get_btc_price(self):
        url = f"{self.base_url}/api/v5/market/ticker"
        params = {
            "instId": "BTC-USDT-SWAP"
        }

        r = requests.get(url, params=params, timeout=10)
        data = r.json()

        return data


if __name__ == "__main__":
    client = OKXClient()
    print(client.get_btc_price())