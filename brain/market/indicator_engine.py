"""
Trading Brain SHD

Indicator Engine V1
"""

import pandas as pd

from brain.market.indicators import (
    add_indicators
)


class IndicatorEngine:

    def __init__(self):

        pass


    def calculate(
        self,
        candles
    ):

        if candles is None:

            return {}


        rows = []


        for c in reversed(candles):

            rows.append(

                {

                    "ts": int(c[0]),

                    "open": float(c[1]),

                    "high": float(c[2]),

                    "low": float(c[3]),

                    "close": float(c[4]),

                    "volume": float(c[5])

                }

            )


        df = pd.DataFrame(rows)


        df = add_indicators(df)


        latest = df.iloc[-1]


        return {

            "ema20": latest["ema20"],

            "ema50": latest["ema50"],

            "rsi": latest["rsi"],

            "atr": latest["atr"],

            "volume_ratio": latest["volume_ratio"]

        }