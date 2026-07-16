from pathlib import Path


from execution.paper_trader import (
    PaperTrader
)


from brain.execution.paper_executor import (
    PaperExecutor
)


from brain.execution.execution_controller import (
    ExecutionController
)



def main():

    print(
        "===== TEST EXECUTION CONTROLLER V2 ====="
    )


    trader = PaperTrader.__new__(
        PaperTrader
    )


    trader.position = None

    trader.history = []


    trader.maker_fee = 0.0002

    trader.taker_fee = 0.0005


    trader.state_file = (
        Path("execution/test_position.json")
    )


    trader.journal_file = (
        Path("execution/test_trade_journal.json")
    )



    if trader.state_file.exists():

        trader.state_file.unlink()



    if trader.journal_file.exists():

        trader.journal_file.unlink()



    paper_executor = PaperExecutor(
        trader
    )


    controller = ExecutionController(
        executor=paper_executor
    )



    result = controller.execute(

        action="OPEN_POSITION",

        data={

            "side": "LONG",

            "entry_price": 65000,

            "size": 0.001,

            "stop_loss": 64500,

            "take_profit": 66000

        }

    )



    print(
        "SUCCESS:",
        result.success
    )


    print(
        "ACTION:",
        result.action
    )


    print(
        "MESSAGE:",
        result.message
    )


    print(
        "TIME:",
        result.timestamp
    )



if __name__ == "__main__":

    main()