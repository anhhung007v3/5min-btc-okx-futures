from execution.okx_trader import OKXTrader
import config


print("===== OKX LEVERAGE TEST =====")

trader = OKXTrader()


result = trader.accountAPI.get_leverage(
    instId=config.SYMBOL,
    mgnMode="cross"
)


print()

print("LEVERAGE RESULT:")

print(result)

print()

print("AVAILABLE METHODS:")

print(
    [x for x in dir(trader.accountAPI) if "lever" in x.lower()]
)