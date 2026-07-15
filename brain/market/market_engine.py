from brain.market.market_state import (
    MarketState
)


class MarketEngine:
    """
    Bộ xử lý trạng thái thị trường SHD.

    Nhiệm vụ:

    - Đánh giá chuyển động thị trường.
    - Cập nhật MarketState.

    Không:
    - Vào lệnh.
    - Quản lý Position.
    """


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
            trend_strength >= 0.5
            and
            volatility >= 0.3
        ):

            state.movement_ok = True


        else:

            state.movement_ok = False



        return state