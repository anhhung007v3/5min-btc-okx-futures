from datetime import datetime


from brain.common.brain_context import (
    BrainContext
)


from brain.monitor.monitor_event import (
    MonitorEvent
)


class BrainLoop:
    def __init__(

        self,

        market_engine,

        decision_engine,

        risk_engine,

        execution_controller,

        brain_monitor

    ):

        self.market_engine = market_engine

        self.decision_engine = decision_engine

        self.risk_engine = risk_engine

        self.execution_controller = execution_controller

        self.brain_monitor = brain_monitor



    def run(

        self,

        context: BrainContext

    ):

        # MARKET

        context.market_state = (

            self.market_engine.evaluate(

                trend_strength=context.trend_strength,

                volatility=context.volatility

            )

        )


        # DECISION

        context.decision = (

            self.decision_engine.evaluate(

                position=context.position,

                market_state=context.market_state

            )

        )


        # RISK

        if context.position is not None:

            context.protection_ok = (

                self.risk_engine.check_protection(

                    context.position

                )

            )


        # EXECUTION

        if (

            context.decision["decision"] == "OPEN"

            and

            context.position is not None

        ):

            context.execution_result = (

                self.execution_controller.open_position(

                    side=context.position.side,

                    price=context.position.entry_price,

                    size=context.position.size,

                    stop_loss=context.position.stop_loss,

                    take_profit=context.position.take_profit

                )

            )


        if self.brain_monitor:

            self.brain_monitor.record(

                MonitorEvent(

                    event_type="BRAIN_CYCLE_COMPLETE",

                    message="CYCLE_FINISHED",

                    timestamp=datetime.utcnow().isoformat(),

                    data={

                        "decision": context.decision,

                        "protection_ok": context.protection_ok

                    }

                )

            )


        return context    