import requests
import pandas as pd


class BTCCandleData:
    def __init__(self):
        self.base_url = "https://www.okx.com"

    def get_candles(self, timeframe="5m", limit=100):
        url = f"{self.base_url}/api/v5/market/candles"

        params = {
            "instId": "BTC-USDT-SWAP",
            "bar": timeframe,
            "limit": limit
        }

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        data = response.json()

        if data["code"] != "0":
            raise Exception(data)

        candles = data["data"]

        df = pd.DataFrame(
            candles,
            columns=[
                "ts",
                "open",
                "high",
                "low",
                "close",
                "volume",
                "volCcy",
                "volCcyQuote",
                "confirm"
            ]
        )

        df["open"] = df["open"].astype(float)
        df["high"] = df["high"].astype(float)
        df["low"] = df["low"].astype(float)
        df["close"] = df["close"].astype(float)
        df["volume"] = df["volume"].astype(float)

        return df


if __name__ == "__main__":
    btc = BTCCandleData()

    print("=== BTC 5 phút ===")
    print(btc.get_candles("5m").head())

    print("\n=== BTC 15 phút ===")
    print(btc.get_candles("15m").head())