from dataclasses import dataclass
from typing import Optional


@dataclass
class MarketState:
    """
    Trạng thái hiện tại của thị trường SHD.

    Không:
    - Vào lệnh.
    - Quản lý Position.

    Chỉ lưu thông tin Market.
    """


    direction: str = "NONE"


    trend_strength: float = 0.0


    volatility: float = 0.0


    movement_ok: bool = False


    timestamp: Optional[str] = None