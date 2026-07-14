import sys
import time
import traceback
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))


from data.btc_candles import BTCCandleData

from strategy.indicators import add_indicators

from strategy.market_condition import analyze_market

from strategy.entry_signal_v16 import check_entry

from strategy.risk_manager_v3 import calculate_risk

from strategy.position_size import calculate_position_size

from execution.paper_trader import PaperTrader

from execution.okx_trader import OKXTrader

import config



class TradingEngine:


    def __init__(self):

        self.btc = BTCCandleData()


        if config.PAPER_MODE:

            self.trader = PaperTrader()

            print(
                "TRADING MODE: PAPER"
            )

        else:

            self.trader = OKXTrader()

            print(
                "TRADING MODE: LIVE"
            )


        self.balance = config.ACCOUNT_SIZE

        self.risk_percent = config.RISK_PERCENT


    def get_market_data(self):

        """
        Lấy dữ liệu BTC 15m và 5m
        """


        df15 = self.btc.get_candles("15m")

        df15 = df15.sort_values("ts")

        df15 = add_indicators(df15)


        market = analyze_market(df15)



        df5 = self.btc.get_candles("5m")

        df5 = df5.sort_values("ts")

        df5 = add_indicators(df5)


        return market, df5



    def run_once(self):

        """
        Chạy một vòng kiểm tra
        """
        
        position = self.trader.get_position()


        if position is not None:

            print("===== EXISTING POSITION =====")

            print(position)


            current_price = float(
                self.btc.get_candles("5m")
                .sort_values("ts")
                .iloc[-1]["close"]
            )


            exit_result = self.trader.check_exit(
                current_price
            )


            print("===== EXIT RESULT =====")

            print(exit_result)


            return

        market, df5 = self.get_market_data()
        # CHECK EXISTING POSITION

        position = self.trader.get_position()


        if position is not None:

            current_price = float(
                df5.iloc[-1]["close"]
            )


            exit_result = self.trader.check_exit(
                current_price
            )


            print("===== EXIT CHECK =====")

            print(exit_result)


            return


        signal = check_entry(
            market,
            df5
        )
    
        
        print("===== SIGNAL =====")

        print(signal)

        if position is not None:

            print()

            print("===== POSITION EXISTS =====")

            print("Skip new entry.")

            return

               

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


            size = calculate_position_size(
                self.balance,
                self.risk_percent,
                signal["price"],
                risk["stop_loss"]
            )


            order = self.trader.open_position(
                side,
                signal["price"],
                size["btc_size"],
                risk["stop_loss"],
                risk["take_profit"]
            )


            print("===== ORDER RESULT =====")

            print(order)

if __name__ == "__main__":


    print("===== TRADING ENGINE START =====")


    engine = TradingEngine()

    while True:

        try:

            engine.run_once()

        except Exception:

            traceback.print_exc()


        print("WAIT 5 MINUTES...")

        time.sleep(300)


    while True:

        try:

            engine.run_once()


        except Exception as e:

            print("===== ENGINE ERROR =====")
            traceback.print_exc()


        print("WAIT 5 MINUTES...")


        time.sleep(300)

