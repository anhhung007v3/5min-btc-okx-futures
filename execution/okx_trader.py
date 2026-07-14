import os

import okx.Account as Account
import okx.MarketData as MarketData
import okx.Trade as Trade

from dotenv import load_dotenv

from execution.trader_interface import TraderInterface

import config


class OKXTrader(TraderInterface):

    def __init__(self):

        load_dotenv()

        self.api_key = os.getenv("OKX_API_KEY")
        self.api_secret = os.getenv("OKX_API_SECRET")
        self.passphrase = os.getenv("OKX_API_PASSPHRASE")
        self.flag = os.getenv("OKX_FLAG")

        self.accountAPI = Account.AccountAPI(
            self.api_key,
            self.api_secret,
            self.passphrase,
            False,
            self.flag
        )

        self.marketAPI = MarketData.MarketAPI(
            flag=self.flag
        )

        self.tradeAPI = Trade.TradeAPI(
            self.api_key,
            self.api_secret,
            self.passphrase,
            False,
            self.flag
        )

        print("OKXTrader initialized.")

    def get_balance(self):

        return self.accountAPI.get_account_balance()

    def get_usdt_balance(self):

        result = self.get_balance()

        details = result["data"][0]["details"]

        for item in details:

            if item["ccy"] == "USDT":

                return float(item["availBal"])

        return 0

    def get_btc_price(self):

        result = self.marketAPI.get_ticker(
            instId="BTC-USDT"
        )

        return float(
            result["data"][0]["last"]
        )

    def get_positions(self):

        return self.accountAPI.get_positions(
            instType="SWAP"
        )

    def get_position(self):

        result = self.get_positions()

        data = result.get(
            "data",
            []
        )

        if len(data) == 0:

            return None

        return data[0]

    def open_position(
        self,
        side,
        entry_price,
        size,
        stop_loss,
        take_profit
    ):

        if config.DRY_RUN:

            print()
            print("========== DRY RUN ==========")
            print(f"SIDE : {side}")
            print(f"ENTRY: {entry_price}")
            print(f"SIZE : {size}")
            print(f"SL   : {stop_loss}")
            print(f"TP   : {take_profit}")
            print("=============================")
            print()

            return {
                "dry_run": True,
                "side": side,
                "entry": entry_price,
                "size": size,
                "stop_loss": stop_loss,
                "take_profit": take_profit
            }

        print("REAL ORDER WILL BE HERE")
        print("NEXT STEP: place_order()")

        result = self.tradeAPI.place_order(
            instId=config.SYMBOL,
            tdMode="cross",
            side="buy" if side == "LONG" else "sell",
            ordType="market",
            sz=str(size)
        )

        print(result)

        return None

    def check_exit(
        self,
        current_price
    ):

        return None