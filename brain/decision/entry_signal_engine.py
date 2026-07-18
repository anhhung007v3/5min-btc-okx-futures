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

        market_state,

        indicators

    ):


        signal = "NO_ENTRY"

        confidence = 0.0



        if indicators is None:


            return {


                "signal": signal,


                "confidence": confidence


            }



        ema20 = indicators["ema20"]

        ema50 = indicators["ema50"]

        rsi = indicators["rsi"]



        if not market_state.movement_ok:


            return {


                "signal": signal,


                "confidence": confidence


            }



        # LONG SETUP

        if (

            ema20 > ema50

            and

            rsi > 50

        ):


            signal = "LONG_READY"


            confidence = 0.70



        # SHORT SETUP

        elif (

            ema20 < ema50

            and

            rsi < 50

        ):


            signal = "SHORT_READY"


            confidence = 0.70



        return {


            "signal": signal,


            "confidence": confidence


        }