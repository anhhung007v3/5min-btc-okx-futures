from brain.position.stage_engine import (
    Stage,
    StageEngine
)

from brain.position.position_state import (
    PositionState
)

from brain.risk.capital_manager import (
    CapitalManager
)


class PositionManager:
    """
    Quản lý một chu kỳ giao dịch SHD.

    Một Position:
    - Có nhiều Entry.
    - Có Stage.
    - Có Risk Data.
    - Có tổng vốn.

    Không:
    - Phân tích thị trường.
    - Tạo tín hiệu.
    """


    def __init__(
        self,
        capital_manager: CapitalManager
    ):

        self.capital_manager = capital_manager

        self.stage_engine = StageEngine()

        self.position = None



    def open_position(
        self,
        side: str,
        price: float,
        size: float,
        capital: float,
        stop_loss: float,
        take_profit: float
    ) -> bool:
        """
        Tạo Position mới.
        """


        if not self.capital_manager.can_open(
            capital
        ):
            return False



        self.capital_manager.add_position(
            capital
        )


        self.position = PositionState(
            side=side,
            stage=Stage.STAGE_0
        )


        self.position.add_entry(
            price=price,
            size=size,
            capital=capital
        )


        self.position.set_risk(
            stop_loss=stop_loss,
            take_profit=take_profit
        )


        return True



    def update_stage(
        self,
        movement_ok: bool,
        protection_ok: bool,
        add_position_ok: bool = False
    ):

        if self.position is None:
            return None



        self.position.stage = (
            self.stage_engine.evaluate_stage(
                current_stage=self.position.stage,
                movement_ok=movement_ok,
                protection_ok=protection_ok,
                add_position_ok=add_position_ok
            )
        )


        return self.position.stage



    def add_position(
        self,
        price: float,
        size: float,
        capital: float
    ) -> bool:
        """
        Thêm Entry vào Position hiện tại.
        """


        if self.position is None:
            return False



        if self.position.stage not in [
            Stage.STAGE_1,
            Stage.STAGE_2
        ]:
            return False



        if not self.capital_manager.can_open(
            capital
        ):
            return False



        self.capital_manager.add_position(
            capital
        )


        self.position.add_entry(
            price=price,
            size=size,
            capital=capital
        )


        return True



    def update_price(
        self,
        current_price: float
    ):
        """
        Cập nhật giá hiện tại của Position.
        """


        if self.position is None:

            return False



        self.position.current_price = current_price


        return True



    def close_position(self):

        self.position = None

        self.capital_manager.used_capital = 0