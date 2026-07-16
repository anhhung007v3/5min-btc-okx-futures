from dataclasses import dataclass

from brain.position.stage_engine import (
    Stage
)


@dataclass
class PositionState:
    """
    Trạng thái Position của SHD.

    Là nguồn dữ liệu duy nhất cho:
    - DecisionEngine
    - RiskEngine
    - ExecutionController
    """

    # Position

    side: str = ""

    stage: Stage = Stage.STAGE_0

    # Prices

    entry_price: float = 0.0

    current_price: float = 0.0

    stop_loss: float = 0.0

    take_profit: float = 0.0

    # Size

    size: float = 0.0

    # Status

    is_open: bool = False