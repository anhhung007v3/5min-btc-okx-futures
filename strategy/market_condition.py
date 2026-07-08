import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from data.btc_candles import BTCCandleData
from strategy.indicators import add_indicators


def analyze_market(df):

    latest = df.iloc[-2]   # chỉ dùng nến đã đóng

    ema20 = latest["ema20"]
    ema50 = latest["ema50"]
    rsi = latest["rsi"]

    volume_ratio = latest["volume_ratio"]

    atr = latest["atr"]


    # Trend
    if ema20 > ema50:
        trend = "LONG"
    elif ema20 < ema50:
        trend = "SHORT"
    else:
        trend = "NEUTRAL"


    # Momentum
    if rsi > 55:
        momentum = "BULLISH"

    elif rsi < 45:
        momentum = "BEARISH"

    else:
        momentum = "NEUTRAL"


    # Volume
    if volume_ratio >= 1.5:
        volume_status = "STRONG"
    elif volume_ratio >= 1.0:
        volume_status = "NORMAL"

    else:
        volume_status = "WEAK"


    # Volatility
    if atr > 200:
        volatility = "HIGH"
    else:
        volatility = "NORMAL"


    # Decision
    if (
        trend == "LONG"
        and momentum == "BULLISH"
        and volume_status == "CONFIRMED"
    ):
        decision = "LOOK_FOR_LONG"

    elif (
        trend == "SHORT"
        and momentum == "BEARISH"
        and volume_status == "CONFIRMED"
    ):
        decision = "LOOK_FOR_SHORT"

    else:
        decision = "WAIT"


    return {
        "trend": trend,
        "momentum": momentum,
        "volume": volume_status,
        "volume_ratio": float(volume_ratio),
        "volatility": volatility,
        "atr": float(atr),
        "decision": decision
    }



if __name__ == "__main__":

    btc = BTCCandleData()

    df = btc.get_candles("15m")

    df = df.sort_values("ts")

    df = add_indicators(df)


    result = analyze_market(df)


    print("===== MARKET CONDITION =====")

    for key, value in result.items():
        print(f"{key}: {value}")