import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))
from data.btc_candles import BTCCandleData
from strategy.indicators import add_indicators
from strategy.market_condition import analyze_market
from strategy.entry_signal import check_entry
from strategy.risk_manager import calculate_risk


btc = BTCCandleData()


# Lấy nến 15m để xác định trend

df15 = btc.get_candles("15m")
df15 = df15.sort_values("ts")
df15 = add_indicators(df15)

market = analyze_market(df15)


# Lấy nến 5m

df5 = btc.get_candles("5m")
df5 = df5.sort_values("ts")
df5 = add_indicators(df5)


signal = check_entry(
    market,
    df5
)


print("===== ENTRY =====")
print(signal)


if signal["signal"] in ["LONG_READY", "SHORT_READY"]:

    candle = df5.iloc[-2]

    side = (
        "LONG"
        if signal["signal"] == "LONG_READY"
        else "SHORT"
    )


    risk = calculate_risk(
        side,
        signal["price"],
        candle["atr"]
    )


    print("===== RISK =====")
    print(risk)


else:

    print("NO TRADE - Risk Manager skipped")