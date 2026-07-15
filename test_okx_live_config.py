from execution.okx_trader import OKXTrader
import config


print("===== OKX LIVE CONFIG CHECK =====")


trader = OKXTrader()


result = trader.accountAPI.get_leverage(
    instId=config.SYMBOL,
    mgnMode="cross"
)


live_leverage = result["data"][0]["lever"]


print()

print("SYMBOL:")
print(config.SYMBOL)

print("CONFIG LEVERAGE:")
print(config.LEVERAGE)

print("OKX LIVE LEVERAGE:")
print(live_leverage)


if str(config.LEVERAGE) == str(live_leverage):

    print()
    print("STATUS: MATCH")

else:

    print()
    print("STATUS: MISMATCH")