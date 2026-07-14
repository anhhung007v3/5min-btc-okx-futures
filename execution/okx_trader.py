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
            instId=config.SYMBOL
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



    def btc_to_contract(
        self,
        btc_size
    ):

        """
        BTC amount -> OKX SWAP contracts

        BTC-USDT-SWAP:
        1 contract = 0.01 BTC
        """

        ct_val = 0.01

        contracts = (
            float(btc_size)
            /
            ct_val
        )

        return round(
            contracts,
            2
        )



    def risk_check(
        self,
        entry_price,
        btc_size
    ):

        available = self.get_usdt_balance()


        notional = (
            float(entry_price)
            *
            float(btc_size)
        )


        margin_required = (
            notional
            /
            config.LEVERAGE
        )


        print()
        print("========== RISK CHECK ==========")

        print(
            f"AVAILABLE FUTURES: {available:.2f} USDT"
        )

        print(
            f"MAX ORDER MARGIN: {config.MAX_MARGIN_PER_TRADE} USDT"
        )

        print(
            f"REQUEST MARGIN: {margin_required:.2f} USDT"
        )


        if available <= 0:

            print(
                "STATUS: BLOCK ORDER"
            )

            print(
                "REASON: NO_BALANCE"
            )

            return False



        if margin_required > config.MAX_MARGIN_PER_TRADE:

            print(
                "STATUS: BLOCK ORDER"
            )

            print(
                "REASON: MAX_MARGIN_EXCEEDED"
            )

            return False



        print(
            "STATUS: RISK CHECK OK"
        )

        print(
            "================================"
        )


        return True



    def open_position(
        self,
        side,
        entry_price,
        size,
        stop_loss,
        take_profit
    ):


        # size đang là BTC

        if not self.risk_check(
            entry_price,
            size
        ):

            return {

                "blocked": True,

                "reason":
                "RISK_CHECK_FAILED"

            }



        contract_size = self.btc_to_contract(
            size
        )


        print()

        print("========== ORDER SIZE ==========")

        print(
            f"BTC SIZE: {size}"
        )

        print(
            f"CONTRACT SIZE: {contract_size}"
        )

        print(
            "================================"
        )



        if config.DRY_RUN:

            print()
            print("========== DRY RUN ==========")

            print(
                f"SIDE : {side}"
            )

            print(
                f"ENTRY: {entry_price}"
            )

            print(
                f"SIZE BTC: {size}"
            )

            print(
                f"SIZE CONTRACT: {contract_size}"
            )

            print(
                f"SL   : {stop_loss}"
            )

            print(
                f"TP   : {take_profit}"
            )

            print(
                "============================="
            )


            return {

                "dry_run": True,

                "side": side,

                "btc_size": size,

                "contract_size": contract_size,

                "stop_loss": stop_loss,

                "take_profit": take_profit

            }



        print(
            "REAL ORDER EXECUTION"
        )


        result = self.tradeAPI.place_order(

            instId=config.SYMBOL,

            tdMode="cross",

            side=(
                "buy"
                if side == "LONG"
                else "sell"
            ),

            ordType="market",

            sz=str(contract_size)

        )


        print(result)


        return result



    def check_exit(
        self,
        current_price
    ):

        return None