from execution.okx_trader import OKXTrader
import config


print("===== OKX GET LEVERAGE TEST =====")


trader = OKXTrader()


leverage = trader.get_leverage()


print()
print("SYMBOL:")
print(config.SYMBOL)

print("LIVE LEVERAGE:")
print(leverage)
