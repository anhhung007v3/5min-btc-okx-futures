from dataclasses import dataclass


@dataclass
class BrainContext:
    """
    Context dùng để truyền dữ liệu
    giữa các Engine trong SHD.
    """

    # Input Market
    trend_strength: float = 0.0
    volatility: float = 0.0

    # Market
    market_state = None

    # Position
    position = None

    # Risk
    protection_ok: bool = False
    profit_percent: float = 0.0

    # Signal
    entry_signal = None

    # Decision
    decision = None
   
    # Execution
    execution_result = None
