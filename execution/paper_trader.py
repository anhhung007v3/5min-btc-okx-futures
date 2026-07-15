import datetime as dt
import json
from pathlib import Path
from typing import Dict, Optional


from execution.trader_interface import TraderInterface


class PaperTrader(TraderInterface):


    def __init__(self):

        self.position = None

        self.history = []

        # OKX Futures fee simulation
        self.maker_fee = 0.0002
        self.taker_fee = 0.0005

        self.state_file = (
            Path(__file__).parent / "position.json"
        )
        self.journal_file = (
            Path(__file__).parent / "trade_journal.json"
        )

        self.load_state()



    def save_state(self):

        data = {

            "position": self.position,

            "history": self.history

        }


        with open(
            self.state_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )


    def save_trade_journal(self, trade):

        journal = []

        if self.journal_file.exists():

            try:

                with open(
                    self.journal_file,
                    "r",
                    encoding="utf-8"
                ) as f:

                    content = f.read().strip()

                    if content:

                        journal = json.loads(content)

            except (
                json.JSONDecodeError,
                OSError
            ):

                journal = []


        journal.append(trade)


        with open(
            self.journal_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                journal,
                f,
                indent=4
            )


    def load_state(self):

        if not self.state_file.exists():

            return

        try:

            with open(
                self.state_file,
                "r",
                encoding="utf-8"
            ) as f:

                content = f.read().strip()

                if not content:

                    return

                data = json.loads(content)

        except (
            json.JSONDecodeError,
            OSError
        ):

            return


        self.position = data.get(
            "position"
        )

        self.history = data.get(
            "history",
            []
        )

    def open_position(
        self,
        side: str,
        entry_price: float,
        size: float,
        stop_loss: float,
        take_profit: float
    ) -> Dict:
        """
        Giả lập mở vị trí.
        """

        if self.position is not None:

            return {
                "status": "ERROR",
                "message": "POSITION_ALREADY_EXISTS"
            }


        self.position = {

            "side": side,

            "entry_price": entry_price,

            "size": size,

            "entry_fee": round(
                entry_price * size * self.taker_fee,
                4
            ),

            "stop_loss": stop_loss,

            "take_profit": take_profit,

            "opened_at": dt.datetime.now().isoformat()

        }

       
        self.save_state()


        return {

            "status": "OPENED",

            "position": self.position

        }



    def get_position(self) -> Optional[Dict]:
        """
        Lấy vị trí hiện tại.
        """

        return self.position

    def close_position(self):

        print()

        print("===== CLOSE POSITION =====")

        self.position = None

        self.save_state()

        return True


    def check_exit(
        self,
        current_price: float
    ) -> Dict:
        """
        Kiểm tra điều kiện thoát lệnh.
        """

        if self.position is None:

            return {
                "status": "NO_POSITION"
            }


        side = self.position["side"]

        stop_loss = self.position["stop_loss"]

        take_profit = self.position["take_profit"]


        result = None


        PRICE_TOLERANCE = 5


        if side == "LONG":

            if current_price <= stop_loss + PRICE_TOLERANCE:

                result = "STOP_LOSS"


            elif current_price >= take_profit - PRICE_TOLERANCE:

                result = "TAKE_PROFIT"



        elif side == "SHORT":

            if current_price >= stop_loss - PRICE_TOLERANCE:

                result = "STOP_LOSS"


            elif current_price <= take_profit + PRICE_TOLERANCE:

                result = "TAKE_PROFIT"



        if result:

            closed_position = self.position.copy()

            closed_position["exit_price"] = current_price

            closed_position["exit_reason"] = result

            if side == "LONG":

                pnl = (
                    current_price
                    - closed_position["entry_price"]
                ) * closed_position["size"]

            else:

                pnl = (
                    closed_position["entry_price"]
                    - current_price
                ) * closed_position["size"]

            closed_position["gross_pnl_usdt"] = round(
                pnl,
                2
            )


            exit_fee = (
                current_price
                * closed_position["size"]
                * self.taker_fee
            )


            closed_position["exit_fee"] = round(
                exit_fee,
                4
            )


            total_fee = (
                closed_position["entry_fee"]
                + closed_position["exit_fee"]
            )


            closed_position["total_fee"] = round(
                total_fee,
                4
            )


            closed_position["net_pnl_usdt"] = round(
                pnl - total_fee,
                2
            )

         

            self.save_trade_journal(
                closed_position
            )
            self.history.append(
                closed_position
            )

            
            self.close_position()


            return {

                "status": "CLOSED",

                "reason": result,

                "exit_price": current_price,

                "position": closed_position

            }


        return {

            "status": "HOLD",

            "current_price": current_price,

            "position": self.position

        }


if __name__ == "__main__":


    print("===== PAPER TRADER TEST =====")


    trader = PaperTrader()


    result = trader.open_position(

        side="SHORT",

        entry_price=62800,

        size=0.055556,

        stop_loss=62980,

        take_profit=62440

    )


    print(result)


    print("CURRENT POSITION:")

    print(
        trader.get_position()
    )
    result = trader.check_exit(
        62440
    )

    print(result)
