from brain.monitor.monitor_event import (
    MonitorEvent
)



class RiskEngine:
    """
    Risk Engine của Trading Brain SHD.

    Nhiệm vụ:

    - Kiểm tra bảo vệ vị thế.
    - Tính lợi nhuận hiện tại.
    - Gửi thông tin cho Monitor.


    Không:

    - Tạo tín hiệu.
    - Mở lệnh.
    - Điều khiển Stage.
    """



    def __init__(
        self,
        monitor=None
    ):

        self.monitor = monitor



    def check_protection(
        self,
        position
    ) -> bool:
        """
        Kiểm tra vị thế đã an toàn chưa.

        LONG:
            Stop >= Entry

        SHORT:
            Stop <= Entry
        """

        side = position.side
        entry_price = position.entry_price
        current_price = position.current_price
        stop_loss = position.stop_loss

        protection_ok = False

        if side == "LONG":

            if stop_loss >= entry_price:

                protection_ok = True

        elif side == "SHORT":

            if stop_loss <= entry_price:

                protection_ok = True

        if self.monitor:

            self.monitor.record(

                MonitorEvent(

                    event_type="RISK_CHECK",

                    message=(
                        "PROTECTION_OK"
                        if protection_ok
                        else "PROTECTION_FAILED"
                    ),

                    timestamp="",

                    data={

                        "side": side,
                        "entry_price": entry_price,
                        "current_price": current_price,
                        "stop_loss": stop_loss

                    }

                )

            )

        return protection_ok



    def calculate_profit_percent(
        self,
        side: str,
        entry_price: float,
        current_price: float
    ) -> float:
        """
        Tính % lợi nhuận hiện tại.
        """


        profit_percent = 0.0



        if side == "LONG":

            profit_percent = (

                (

                    current_price

                    -

                    entry_price

                )

                /

                entry_price

            ) * 100



        elif side == "SHORT":

            profit_percent = (

                (

                    entry_price

                    -

                    current_price

                )

                /

                entry_price

            ) * 100



        if self.monitor:


            self.monitor.record(

                MonitorEvent(

                    event_type="RISK_PROFIT",

                    message="PROFIT_CALCULATED",

                    timestamp="",

                    data={

                        "side": side,

                        "profit_percent": profit_percent

                    }

                )

            )



        return profit_percent