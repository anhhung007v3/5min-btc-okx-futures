import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from data.btc_candles import BTCCandleData
from strategy.indicators import add_indicators
from strategy.market_condition import analyze_market


def check_entry(market, df5):

    candle = df5.iloc[-2]   # chỉ dùng nến đã đóng

    score = 0

    details = {}


    close = candle["close"]
    open_price = candle["open"]
    high = candle["high"]
    low = candle["low"]

    ema20 = candle["ema20"]

    volume_ratio = candle["volume_ratio"]


    # ======================
    # 1. TREND CHECK
    # ======================

    trend = market["trend"]

    if trend in ["LONG", "SHORT"]:
        score += 2
        details["trend"] = trend
    else:
        details["trend"] = "NEUTRAL"



    # ======================
    # 2. PULLBACK CHECK
    # ======================

    distance = abs(close - ema20) / ema20


    if distance < 0.003:

        score += 2
        details["pullback"] = "YES"

    else:

        details["pullback"] = "NO"



    # ======================
    # 3. REJECTION CANDLE
    # ======================

    body = abs(close - open_price)

    upper_wick = high - max(
        open_price,
        close
    )

    lower_wick = min(
        open_price,
        close
    ) - low



    rejection = False


    # SHORT rejection

    if trend == "SHORT":

        if (
            close < open_price
            and upper_wick >= body * 0.7
        ):
            rejection = True



    # LONG rejection

    if trend == "LONG":

        if (
            close > open_price
            and lower_wick >= body * 0.7
        ):
            rejection = True



    if rejection:

        score += 2
        details["rejection"] = "YES"

    else:

        details["rejection"] = "NO"



    # ======================
    # 4. VOLUME CHECK
    # ======================

    if volume_ratio >= 1.2:

        score += 2
        details["volume"] = "STRONG"

    else:

        details["volume"] = "WEAK"



    # ======================
    # FINAL DECISION
    # ======================

    if score == 8:

        if trend == "SHORT":
            signal = "SHORT_READY"

        elif trend == "LONG":
            signal = "LONG_READY"

        else:
            signal = "NO_ENTRY"

    else:

        signal = "NO_ENTRY"



    return {

        "signal": signal,

        "score": f"{score}/8",

        "details": details,

        "price": float(close),

        "volume_ratio": float(volume_ratio),
        "ema20": float(ema20),
        "candle": {
             "open": float(open_price),
             "high": float(high),
             "low": float(low),
             "close": float(close)
        }

    }



if __name__ == "__main__":


    btc = BTCCandleData()


    # 15m trend

    df15 = btc.get_candles("15m")

    df15 = df15.sort_values("ts")

    df15 = add_indicators(df15)


    market = analyze_market(df15)



    # 5m entry

    df5 = btc.get_candles("5m")

    df5 = df5.sort_values("ts")

    df5 = add_indicators(df5)


    result = check_entry(
        market,
        df5
    )


    print("===== ENTRY SIGNAL V3 =====")

    print(result)