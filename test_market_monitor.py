from brain.market.market_engine import (
    MarketEngine
)


from brain.monitor.brain_monitor import (
    BrainMonitor
)



def main():

    print(
        "===== TEST MARKET MONITOR ====="
    )


    monitor = BrainMonitor(
        log_file="test_market_monitor.log"
    )


    market_engine = MarketEngine(
        monitor=monitor
    )


    state = market_engine.evaluate(

        trend_strength=0.7,

        volatility=0.5

    )


    print(
        "MOVEMENT OK:",
        state.movement_ok
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