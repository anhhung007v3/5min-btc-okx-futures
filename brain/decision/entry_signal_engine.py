"""
Trading Brain SHD

Entry Signal Engine V1

Detect possible trade opportunity.
"""


class EntrySignalEngine:
    """
    Entry signal layer.

    Không:
    - mở lệnh
    - quản lý position
    - quản lý risk
    """


    def __init__(
        self,
        monitor=None
    ):

        self.monitor = monitor



    def evaluate(
        self,
        market_state
    ):

        signal = "NO_ENTRY"
        confidence = 0.0


        if market_state.movement_ok:

            if market_state.trend_strength >= 0.7:

                signal = "LONG_READY"

                confidence = (
                    market_state.trend_strength
                )


        return {

            "signal": signal,

            "confidence": confidence

        }