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
        "===== TEST RISK MONITOR ====="
    )


    monitor = BrainMonitor(
        log_file="test_risk_monitor.log"
    )


    risk_engine = RiskEngine(
        monitor=monitor
    )


    position = PositionState()

    position.side = "LONG"

    position.entry_price = 60000

    position.current_price = 60500

    position.stop_loss = 60000


    result = risk_engine.check_protection(

        position

    )

    print(
        "PROTECTION OK:",
        result
    )



    profit = risk_engine.calculate_profit_percent(

        side="LONG",

        entry_price=60000,

        current_price=60600

    )


    print(
        "PROFIT %:",
        round(profit, 2)
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