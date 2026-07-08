from indicators import add_indicators


def analyze_trend(df):
    latest = df.iloc[-2]  # lấy nến đã đóng, bỏ nến đang chạy

    ema20 = latest["ema20"]
    ema50 = latest["ema50"]
    rsi = latest["rsi"]

    if ema20 > ema50 and rsi > 45:
        return {
            "trend": "LONG",
            "ema20": ema20,
            "ema50": ema50,
            "rsi": rsi
        }

    elif ema20 < ema50 and rsi < 55:
        return {
            "trend": "SHORT",
            "ema20": ema20,
            "ema50": ema50,
            "rsi": rsi
        }

    else:
        return {
            "trend": "NEUTRAL",
            "ema20": ema20,
            "ema50": ema50,
            "rsi": rsi
        }


if __name__ == "__main__":

    import sys
    from pathlib import Path

    ROOT = Path(__file__).resolve().parent.parent
    sys.path.append(str(ROOT))

    from data.btc_candles import BTCCandleData

    btc = BTCCandleData()

    df = btc.get_candles("15m")

    df = df.sort_values("ts")

    df = add_indicators(df)

    result = analyze_trend(df)

    print("===== BTC TREND ANALYSIS =====")
    print(result)