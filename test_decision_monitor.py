from brain.decision.decision_engine import (
    DecisionEngine
)


from brain.monitor.brain_monitor import (
    BrainMonitor
)


from brain.market.market_state import (
    MarketState
)



def main():

    print(
        "===== TEST DECISION MONITOR ====="
    )


    monitor = BrainMonitor(
        log_file="test_decision_monitor.log"
    )


    decision_engine = DecisionEngine(
        monitor=monitor
    )


    market_state = MarketState()

    market_state.movement_ok = True



    result = decision_engine.evaluate(

        position=None,

        market_state=market_state

    )



    print(
        "DECISION:",
        result["decision"]
    )


    print(
        "REASON:",
        result["reason"]
    )



    events = monitor.get_events()



    print(
        "EVENT COUNT:",
        len(events)
    )


    print(
        "EVENT:",
        events[0].event_type
    )


    print(
        "MESSAGE:",
        events[0].message
    )



if __name__ == "__main__":

    main()