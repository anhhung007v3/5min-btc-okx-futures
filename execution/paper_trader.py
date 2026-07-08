import datetime as dt
import json
from pathlib import Path
from typing import Dict, Optional


class PaperTrader:


    def __init__(self):

        self.position = None

        self.history = []

        self.state_file = (
            Path(__file__).parent / "position.json"
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



    def load_state(self):

        if self.state_file.exists():

            with open(
                self.state_file,
                "r",
                encoding="utf-8"
            ) as f:

                data = json.load(f)


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

            "stop_loss": stop_loss,

            "take_profit": take_profit,

            "opened_at": dt.datetime.now().isoformat()

        }


        self.history.append(
            self.position.copy()
        )
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


            self.history.append(
                closed_position
            )


            self.position = None
            self.save_state()


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
