from execution.okx_trader import OKXTrader
import config
config.DRY_RUN = False

print("===== REAL ORDER LOCK TEST =====")

trader = OKXTrader()


print()

print("DRY_RUN:", config.DRY_RUN)

print(
    "ALLOW_REAL_ORDER:",
    config.ALLOW_REAL_ORDER
)


print()


result = trader.open_position(

    side="LONG",

    entry_price=62500,

    size=0.001,

    stop_loss=62300,

    take_profit=62900

)


print()

print("RESULT:")

print(result)