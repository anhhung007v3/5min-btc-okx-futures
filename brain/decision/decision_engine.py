from brain.position.stage_engine import (
    Stage
)


from brain.monitor.monitor_event import (
    MonitorEvent
)



class DecisionEngine:
    """
    Decision Brain SHD V1.

    Nhiệm vụ:

    - Kết hợp Market + Position.
    - Đưa ra quyết định cấp cao.
    - Gửi event cho Monitor.


    Không:

    - Gửi lệnh.
    - Quản lý vốn.
    - Tính Risk.
    """



    def __init__(
        self,
        monitor=None
    ):

        self.monitor = monitor


    def evaluate(
        self,
        position,
        market_state,
        entry_signal=None
    ):

        decision = None

        reason = None


        if position is None:

            if entry_signal:

                if entry_signal["signal"] in [
                    "LONG_READY",
                    "SHORT_READY"
                ]:

                    decision = "OPEN"

                    reason = entry_signal["signal"]


                else:

                    decision = "WAIT"

                    reason = "NO_ENTRY"


            else:

                decision = "WAIT"

                reason = "NO_SIGNAL"



        elif market_state.movement_ok:


            if position.stage == Stage.STAGE_0:

                decision = "HOLD"

                reason = "WAIT_PROTECTION"



            elif position.stage == Stage.STAGE_1:

                decision = "DEVELOP"

                reason = "POSITION_SAFE"



            elif position.stage == Stage.STAGE_2:

                decision = "MANAGE"

                reason = "PROFIT_PROTECTION"



        else:

            decision = "HOLD"

            reason = "MARKET_NOT_READY"



        if self.monitor:


            self.monitor.record(

                MonitorEvent(

                    event_type="DECISION_MADE",

                    message=decision,

                    timestamp="",

                    data={

                        "reason": reason

                    }

                )

            )


        return {

            "decision": decision,

            "reason": reason

        }