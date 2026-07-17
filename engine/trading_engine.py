import sys
import time
import os
import logging
from datetime import datetime
import traceback
from datetime import datetime
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

    def write_log(self, data):

        with open(
            "project_logs/paper_trading/engine_log.txt",
            "a",
            encoding="utf-8"
        ) as f:

            f.write(
                "\n\n"
                + "=" * 50
                + "\n"
            )

            f.write(
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                + "\n"
            )

            f.write(
                str(data)
                +
                "\n"
            )


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



            print("===== EXIT RESULT =====")

            print(exit_result)

            self.write_log({
                "position": position,
                "exit_result": exit_result
            })


            if exit_result is not None:


                if exit_result.get("exit"):


                    print()

                    print("===== POSITION CLOSED =====")

                    print(
                        exit_result["reason"]
                    )


                    self.trader.position = None


            return
        market, df5 = self.get_market_data()


        signal = check_entry(
            market,
            df5
        )


        print("===== SIGNAL =====")

        print(signal)
        self.write_log(signal)

              

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


            if config.PAPER_MODE:

                leverage = config.LEVERAGE

            else:

                leverage = self.trader.get_leverage()



            size = calculate_position_size(
                self.balance,
                self.risk_percent,
                signal["price"],
                risk["stop_loss"],
                leverage
            )
            metadata = {
                "market": market,
                "signal": signal,
                "risk": risk,
                "size": size
            }

            order = self.trader.open_position(
                side,
                signal["price"],
                size["btc_size"],
                risk["stop_loss"],
                risk["take_profit"],
                metadata
            )

            print("===== ORDER RESULT =====")

            print(order)

            self.write_log({

                "market": market,

                "signal": signal,

                "risk": risk,

                "size": size,

                "order": order

            })

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


    
