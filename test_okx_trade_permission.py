from execution.okx_trader import OKXTrader

print("===== OKX TRADE PERMISSION TEST =====")

trader = OKXTrader()

print()

result = trader.tradeAPI.get_orders_history(
    instType="SWAP",
    instId="BTC-USDT-SWAP",
    limit="5"
)

print(result)