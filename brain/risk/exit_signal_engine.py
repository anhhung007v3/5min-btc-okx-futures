"""
Trading Brain SHD

Exit Signal Engine V1

Detect when current position should exit.
"""


class ExitSignalEngine:
    """
    Exit decision support layer.

    Nhiệm vụ:
    - Kiểm tra Take Profit.
    - Kiểm tra Stop Loss.
    - Trả tín hiệu thoát.

    Không:
    - Đóng lệnh.
    - Gửi execution.
    - Quản lý position.
    """


    def __init__(
        self,
        monitor=None
    ):

        self.monitor = monitor



    def evaluate(
        self,
        position,
        current_price
    ):

        if position is None:

            return {

                "exit": False,

                "reason": "NO_POSITION"

            }



        exit_signal = False

        reason = "HOLD"



        if position.side == "LONG":


            if current_price >= position.take_profit:

                exit_signal = True

                reason = "TAKE_PROFIT"



            elif current_price <= position.stop_loss:

                exit_signal = True

                reason = "STOP_LOSS"



        elif position.side == "SHORT":


            if current_price <= position.take_profit:

                exit_signal = True

                reason = "TAKE_PROFIT"



            elif current_price >= position.stop_loss:

                exit_signal = True

                reason = "STOP_LOSS"



        return {

            "exit": exit_signal,

            "reason": reason

        }