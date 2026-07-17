"""
Trading Brain SHD
BrainLoop V1 Test
"""


from brain.brain_loop import BrainLoop
from brain.common.brain_context import BrainContext



class FakeMarketEngine:

    def evaluate(
        self,
        trend_strength,
        volatility
    ):

        return {
            "market": "GOOD"
        }



class FakeDecisionEngine:

    def evaluate(
        self,
        position,
        market_state
    ):

        return {
            "decision": "OPEN"
        }



class FakeRiskEngine:

    def check_protection(
        self,
        position
    ):

        return True



class FakeExecutionController:

    def __init__(self):

        self.called = False


    def open_position(
        self,
        side,
        price,
        size,
        stop_loss,
        take_profit
    ):

        self.called = True

        return {
            "status": "EXECUTED"
        }



class FakeMonitor:

    pass



class FakePosition:

    side = "LONG"

    entry_price = 65000

    size = 0.001

    stop_loss = 64000

    take_profit = 67000



def main():

    print("===== TEST BRAIN LOOP V1 =====")


    execution = FakeExecutionController()


    brain_loop = BrainLoop(

        FakeMarketEngine(),

        FakeDecisionEngine(),

        FakeRiskEngine(),

        execution,

        FakeMonitor()

    )


    context = BrainContext()


    context.position = FakePosition()


    result = brain_loop.run(context)


    print("MARKET:")
    print(result.market_state)


    print("DECISION:")
    print(result.decision)


    print("RISK:")
    print(result.protection_ok)


    print("EXECUTION CALLED:")
    print(execution.called)



if __name__ == "__main__":

    main()