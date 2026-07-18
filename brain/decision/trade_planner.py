"""
Trading Brain SHD

Trade Planner V1

Create trade parameters after OPEN decision.
"""


class TradePlanner:
    """
    Tạo kế hoạch giao dịch.

    Không:
    - gửi lệnh
    - mở position
    - quản lý risk
    """


    def __init__(
        self,
        capital=5.0
    ):

        self.capital = capital



    def create_plan(
        self,
        signal,
        price
    ):

        if signal["signal"] == "LONG_READY":

            return {

                "side": "LONG",

                "price": price,

                "size": 0.001,

                "capital": self.capital,

                "stop_loss": price - 500,

                "take_profit": price + 1000

            }


        if signal["signal"] == "SHORT_READY":

            return {

                "side": "SHORT",

                "price": price,

                "size": 0.001,

                "capital": self.capital,

                "stop_loss": price + 500,

                "take_profit": price - 1000

            }


        return None