from brain.market.market_state import (
    MarketState
)


from brain.monitor.monitor_event import (
    MonitorEvent
)



class MarketEngine:
    """
    Bộ xử lý trạng thái thị trường SHD.

    Nhiệm vụ:

    - Đánh giá chuyển động thị trường.
    - Cập nhật MarketState.
    - Gửi thông tin cho Monitor.

    Không:
    - Vào lệnh.
    - Quản lý Position.
    """


    def __init__(
        self,
        monitor=None
    ):

        self.monitor = monitor



    def evaluate(
        self,
        trend_strength: float,
        volatility: float
    ) -> MarketState:
        """
        Đánh giá Market.

        Quy tắc V1:

        Trend >= 0.5
        Volatility >= 0.3

        => movement_ok
        """


        state = MarketState()


        state.trend_strength = trend_strength


        state.volatility = volatility



        if (
            trend_strength >= 0.000005
            and
            volatility >= 0.00001
        ):

            state.movement_ok = True


        else:

            state.movement_ok = False



        if self.monitor:


            self.monitor.record(

                MonitorEvent(

                    event_type="MARKET_UPDATE",

                    message="MARKET_EVALUATED",

                    timestamp="",

                    data={

                        "trend_strength": trend_strength,

                        "volatility": volatility,

                        "movement_ok": state.movement_ok

                    }

                )

            )



        return state