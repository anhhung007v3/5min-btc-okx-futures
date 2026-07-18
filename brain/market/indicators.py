import pandas as pd


def calculate_ema(df, period):
    return df["close"].ewm(
        span=period,
        adjust=False
    ).mean()


def calculate_rsi(df, period=14):
    delta = df["close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss

    return 100 - (100 / (1 + rs))


def calculate_atr(df, period=14):

    high_low = df["high"] - df["low"]

    high_close = (
        df["high"] - df["close"].shift()
    ).abs()

    low_close = (
        df["low"] - df["close"].shift()
    ).abs()

    true_range = pd.concat(
        [
            high_low,
            high_close,
            low_close
        ],
        axis=1
    ).max(axis=1)

    return true_range.rolling(period).mean()


def add_indicators(df):

    df = df.copy()

    df["ema20"] = calculate_ema(df, 20)
    df["ema50"] = calculate_ema(df, 50)

    df["rsi"] = calculate_rsi(df)

    df["volume_ma"] = (
        df["volume"]
        .rolling(20)
        .mean()
    )
    df["volume_ratio"] = (
        df["volume"] /
        df["volume_ma"]
    )
    df["atr"] = calculate_atr(df)

    return df


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

    print(df.tail(5))