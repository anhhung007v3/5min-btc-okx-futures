from execution.okx_trader import OKXTrader


print("===== OKX CONTRACT TEST =====")


trader = OKXTrader()


print()
print("CURRENT FUTURES BALANCE:")
print(
    trader.get_usdt_balance()
)


print()
print("===== TEST NORMAL ORDER =====")


result = trader.open_position(

    side="LONG",

    entry_price=62500,

    size=0.001,

    stop_loss=62300,

    take_profit=62900

)


print()
print("===== RESULT =====")
print(result)