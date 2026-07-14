from execution.okx_trader import OKXTrader
from strategy.risk_manager_v3 import calculate_risk
from strategy.position_size import calculate_position_size
import config


print("===== FULL EXECUTION TEST =====")


trader = OKXTrader()


entry = 62500
side = "LONG"


risk = calculate_risk(
    side,
    entry,
    200
)


print()
print("RISK:")
print(risk)


size = calculate_position_size(
    config.ACCOUNT_SIZE,
    config.RISK_PERCENT,
    entry,
    risk["stop_loss"]
)


print()
print("SIZE:")
print(size)


result = trader.open_position(
    side,
    entry,
    size["btc_size"],
    risk["stop_loss"],
    risk["take_profit"]
)


print()
print("ORDER RESULT:")
print(result)