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

        r = requests.get(
            url,
            params=params,
            timeout=10
        )

        return r.json()


    def get_candles(
        self,
        bar="5m",
        limit=100
    ):

        url = (
            f"{self.base_url}"
            "/api/v5/market/candles"
        )

        params = {

            "instId": "BTC-USDT-SWAP",

            "bar": bar,

            "limit": limit

        }

        r = requests.get(
            url,
            params=params,
            timeout=10
        )

        return r.json()


if __name__ == "__main__":

    client = OKXClient()

    print(client.get_btc_price())