from dataclasses import dataclass
from typing import Optional

from brain.common.states import (
    MarketState,
    DecisionState,
    PositionState
)


@dataclass
class MarketContext:
    """
    Thông tin thị trường sau khi Market Brain phân tích.
    """

    symbol: str
    timeframe: str

    market_state: MarketState

    price: float

    atr: float

    volume_ratio: float


@dataclass
class DecisionContext:
    """
    Quyết định của Decision Brain.
    """

    decision: DecisionState

    reason: str


@dataclass
class PositionContext:
    """
    Trạng thái vị thế hiện tại.
    """

    position_state: PositionState

    side: Optional[str]

    entry_price: Optional[float]

    size: float


@dataclass
class RiskContext:
    """
    Kết quả đánh giá rủi ro.
    """

    allow_trade: bool

    reason: str