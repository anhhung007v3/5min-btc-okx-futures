from brain.brain_loop import (
    BrainLoop
)

from brain.common.brain_context import (
    BrainContext
)

from brain.market.market_engine import (
    MarketEngine
)

from brain.decision.decision_engine import (
    DecisionEngine
)

from brain.risk.risk_engine import (
    RiskEngine
)

from brain.monitor.brain_monitor import (
    BrainMonitor
)

from brain.position.position_state import (
    PositionState
)



def main():

    print(
        "===== TEST BRAIN LOOP V1 ====="
    )


    monitor = BrainMonitor(
        log_file="test_brain_loop.log"
    )


    brain_loop = BrainLoop(

        market_engine=MarketEngine(
            monitor=monitor
        ),

        decision_engine=DecisionEngine(
            monitor=monitor
        ),

        risk_engine=RiskEngine(
            monitor=monitor
        ),

        execution_controller=None,

        brain_monitor=monitor

    )


    position = PositionState()

    position.side = "LONG"

    position.entry_price = 60000

    position.current_price = 60500

    position.stop_loss = 60000



    context = BrainContext()

    context.position = position

    context.trend_strength = 0.8

    context.volatility = 0.5



    result = brain_loop.run(
        context
    )


    print(
        "MARKET OK:",
        result.market_state.movement_ok
    )


    print(
        "DECISION:",
        result.decision["decision"]
    )


    print(
        "PROTECTION:",
        result.protection_ok
    )


    events = monitor.get_events()


    print(
        "EVENT COUNT:",
        len(events)
    )


    for event in events:

        print(
            "EVENT:",
            event.event_type
        )

        print(
            "MESSAGE:",
            event.message
        )



if __name__ == "__main__":

    main()