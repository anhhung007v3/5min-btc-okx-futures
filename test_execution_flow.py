from brain.execution.execution_controller import (
    ExecutionController
)

from brain.execution.paper_executor import (
    PaperExecutor
)


class DummyPaperTrader:


    def open_position(
        self,
        side,
        entry_price,
        size,
        stop_loss,
        take_profit
    ):

        print(
            "PAPER OPEN:",
            side,
            entry_price,
            size
        )

        return {

            "status": "OPENED"

        }



def main():

    print(
        "START EXECUTION FLOW TEST"
    )


    paper_trader = DummyPaperTrader()


    executor = PaperExecutor(
        paper_trader
    )


    controller = ExecutionController(
        executor
    )


    result = controller.open_position(

        side="LONG",

        price=62500,

        size=0.001,

        stop_loss=62000,

        take_profit=63500

    )


    print(
        "RESULT:",
        result
    )


    assert result.success is True


    print(
        "EXECUTION_FLOW_TEST_PASS"
    )



if __name__ == "__main__":
    main()