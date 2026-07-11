import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from data.btc_candles import BTCCandleData
from strategy.indicators import add_indicators
from strategy.market_condition import analyze_market
# =========================
# Strategy Configuration
# =========================

PULLBACK_DISTANCE = 0.003
REJECTION_RATIO = 0.7
MIN_VOLUME_RATIO = 1.2
MAX_SCORE = 8

SIGNAL_LONG = "LONG_READY"
SIGNAL_SHORT = "SHORT_READY"
SIGNAL_NONE = "NO_ENTRY"
TREND_LONG = "LONG"
TREND_SHORT = "SHORT"
def check_trend(trend: str) -> tuple[int, str]:
    """
    Kiểm tra xu hướng thị trường.
    Trả về:
        (score, trend_result)
    """
    if trend in (TREND_LONG, TREND_SHORT):
        return 2, trend

    return 0, "NEUTRAL"
def check_pullback(
    close: float,
    ema20: float
) -> tuple[int, str]:
    """
    Kiểm tra giá hồi về EMA20.
    """
    distance = abs(close - ema20) / ema20
    if distance < PULLBACK_DISTANCE:
        return 2, "YES"

    return 0, "NO"
def check_rejection(
    trend: str,
    open_price: float,
    close: float,
    high: float,
    low: float
) -> tuple[int, str]:
    """
    Kiểm tra nến rejection theo hướng trend.
    """

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


    if trend == TREND_SHORT:

        if (
            close < open_price
            and upper_wick >= body * REJECTION_RATIO
        ):
            rejection = True


    if trend == TREND_LONG:

        if (
            close > open_price
            and lower_wick >= body * REJECTION_RATIO
        ):
            rejection = True


    if rejection:
        return 2, "YES"

    return 0, "NO"
def check_volume(
    volume_ratio: float
) -> tuple[int, str]:
    """
    Kiểm tra sức mạnh volume.
    """

    
      
    return 0, "WEAK"


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

    trend_score, trend_result = check_trend(trend)

    score += trend_score
    details["trend"] = trend_result
    


    # ======================
    # 2. PULLBACK CHECK
    # ======================

    pullback_score, pullback_result = check_pullback(
    close,
    ema20
    )

    score += pullback_score
    details["pullback"] = pullback_result



    # ======================
    # 3. REJECTION CANDLE
    # ======================

    
    rejection_score, rejection_result = check_rejection(
    trend,
    open_price,
    close,
    high,
    low
    )

    score += rejection_score
    details["rejection"] = rejection_result

    volume_score, volume_result = check_volume(
        volume_ratio
    )

    score += volume_score
    details["volume"] = volume_result



    # ======================
    # FINAL DECISION
    # ======================

    if score == MAX_SCORE:

        if trend == TREND_SHORT:
            signal = SIGNAL_SHORT

        elif trend == TREND_LONG:
            signal = SIGNAL_LONG

        else:
            signal = "NO_ENTRY"

    else:

        signal = SIGNAL_NONE



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