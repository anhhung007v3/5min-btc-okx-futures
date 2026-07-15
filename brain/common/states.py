from enum import Enum


class MarketState(Enum):
    """
    Trạng thái của thị trường.
    """

    SLEEP = "SLEEP"
    SIDEWAY = "SIDEWAY"
    UPTREND = "UPTREND"
    DOWNTREND = "DOWNTREND"
    BREAKOUT = "BREAKOUT"
    REVERSAL = "REVERSAL"


class DecisionState(Enum):
    """
    Quyết định của Trading Brain.
    """

    WAIT = "WAIT"
    OPEN_LONG = "OPEN_LONG"
    OPEN_SHORT = "OPEN_SHORT"
    ADD_POSITION = "ADD_POSITION"
    MOVE_STOP = "MOVE_STOP"
    EXIT = "EXIT"


class PositionState(Enum):
    """
    Trạng thái vị thế.
    """

    NONE = "NONE"
    OPEN = "OPEN"
    PROTECTED = "PROTECTED"
    PYRAMID = "PYRAMID"
    CLOSED = "CLOSED"