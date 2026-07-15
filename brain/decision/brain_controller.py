from brain.risk.risk_engine import (
    RiskEngine
)

from brain.position.position_manager import (
    PositionManager
)

from brain.position.stage_engine import (
    Stage
)


class BrainController:
    """
    Bộ điều phối Trading Brain SHD.

    Nhiệm vụ:

    - Kết nối Risk.
    - Cập nhật Stage.
    - Quyết định có thể phát triển Position hay không.

    Không:
    - Phân tích thị trường.
    - Tạo tín hiệu.
    - Gửi lệnh.
    """


    def __init__(
        self,
        position_manager: PositionManager
    ):

        self.position_manager = position_manager

        self.risk_engine = RiskEngine()



    def evaluate_position(
        self,
        current_price: float
    ):
        """
        Đánh giá Position hiện tại.
        """


        position = self.position_manager.position


        if position is None:
            return None



        protection_ok = self.risk_engine.check_protection(
            side=position.side,
            entry_price=position.average_price,
            current_price=current_price,
            stop_loss=position.stop_loss
        )


        stage = self.position_manager.update_stage(
            movement_ok=True,
            protection_ok=protection_ok
        )


        return {
            "stage": stage,
            "protection_ok": protection_ok
        }