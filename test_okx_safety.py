from execution.okx_trader import OKXTrader


print("===== OKX SAFETY BLOCK TEST =====")


trader = OKXTrader()


print()
print("CURRENT FUTURES BALANCE:")
print(
    trader.get_usdt_balance()
)


print()
print("===== TEST OVERSIZE ORDER =====")


result = trader.open_position(

    side="LONG",

    entry_price=62500,

    size=0.01,

    stop_loss=62000,

    take_profit=63500

)


print()
print("===== RESULT =====")
print(result)