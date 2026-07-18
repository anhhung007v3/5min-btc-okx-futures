from execution.paper_trader import PaperTrader

from brain.execution.paper_executor import PaperExecutor
from brain.execution.execution_controller import ExecutionController


def main():

    print("START CLOSE POSITION FLOW TEST")


    paper_trader = PaperTrader()


    executor = PaperExecutor(
        paper_trader
    )


    controller = ExecutionController(
        executor=executor
    )


    # OPEN MOCK POSITION

    paper_trader.open_position(
        side="LONG",
        entry_price=62500,
        size=0.001,
        stop_loss=62000,
        take_profit=63500
    )


    print(
        "BEFORE CLOSE:",
        paper_trader.get_position()
    )


    result = executor.execute(
        action="CLOSE_POSITION",
        data={}
    )


    print(
        "RESULT:",
        result
    )


    print(
        "AFTER CLOSE:",
        paper_trader.get_position()
    )


    assert result.success == True


    print(
        "CLOSE_POSITION_FLOW_TEST_PASS"
    )


if __name__ == "__main__":

    main()