"""
Trading Brain SHD

Brain Decision Flow V1

Test:
Market -> Decision -> Execution -> PaperTrader
"""


from brain.runtime.runtime_controller import RuntimeController
from brain.position.position_state import PositionState



def main():

    print(
        "START BRAIN DECISION FLOW TEST"
    )


    controller = RuntimeController()


    controller.startup()


    # Inject market

    controller.context.trend_strength = 0.8
    controller.context.volatility = 0.6


    # Inject fake position

    controller.context.position = PositionState(

        side="LONG",

        entry_price=64000,

        current_price=64050,

        stop_loss=63500,

        take_profit=65000,

        size=0.001,

        is_open=True

    )


    print(
        "RUN DECISION FLOW"
    )


    context = controller.run_cycle()


    print(
        "MARKET:",
        context.market_state
    )


    print(
        "DECISION:",
        context.decision
    )


    print(
        "EXECUTION:",
        context.execution_result
    )


    print(
        "POSITION:",
        controller.paper_trader.get_position()
    )


    controller.shutdown()


    print(
        "BRAIN_DECISION_FLOW_TEST_PASS"
    )



if __name__ == "__main__":
    main()