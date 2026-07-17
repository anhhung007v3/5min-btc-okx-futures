from execution.paper_trader import PaperTrader

from brain.execution.paper_executor import (
    PaperExecutor
)

from brain.execution.execution_controller import (
    ExecutionController
)


print("===== FULL SHD PAPER EXECUTION TEST =====")


trader = PaperTrader()


paper_executor = PaperExecutor(
    trader
)


controller = ExecutionController(
    executor=paper_executor
)


result = controller.open_position(

    side="LONG",

    price=62500,

    size=0.001,

    stop_loss=62000,

    take_profit=63500

)


print()

print("SUCCESS:")
print(result.success)


print()

print("ACTION:")
print(result.action)


print()

print("MESSAGE:")
print(result.message)


print()

print("POSITION:")
print(trader.get_position())