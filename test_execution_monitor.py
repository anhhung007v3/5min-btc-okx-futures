from execution.paper_trader import PaperTrader

from brain.execution.paper_executor import (
    PaperExecutor
)

from brain.execution.execution_controller import (
    ExecutionController
)

from brain.monitor.brain_monitor import (
    BrainMonitor
)


def main():

    print("===== TEST EXECUTION MONITOR =====")

    monitor = BrainMonitor(
        log_file="test_execution_monitor.log"
    )

    trader = PaperTrader()

    trader.position = None
    trader.save_state()

    executor = PaperExecutor(
        paper_trader=trader
    )

    controller = ExecutionController(
        executor=executor,
        monitor=monitor
    )

    result = controller.open_position(

        side="LONG",

        price=60000,

        size=0.001,

        stop_loss=59500,

        take_profit=61000

    )

    print("SUCCESS:", result.success)
    print("ACTION:", result.action)
    print("MESSAGE:", result.message)

    events = monitor.get_events()

    print("EVENT COUNT:", len(events))

    for event in events:

        print("EVENT:", event.event_type)
        print("MESSAGE:", event.message)


if __name__ == "__main__":
    main()