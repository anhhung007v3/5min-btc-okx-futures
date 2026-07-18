from brain.runtime.runtime_controller import (
    RuntimeController
)


from brain.common.brain_context import (
    BrainContext
)


def main():

    print(
        "START FULL TRADE LIFECYCLE TEST"
    )


    controller = RuntimeController()


    context = controller.context


    # =========================
    # STEP 1: MARKET + ENTRY
    # =========================

    context.trend_strength = 0.8

    context.volatility = 0.6


    print("\nSTEP 1 - OPEN")


    result = controller.run_cycle()


    print(
        "DECISION:",
        result.decision
    )


    print(
        "POSITION:",
        result.position
    )


    assert result.position is not None



    # =========================
    # STEP 2: SIMULATE TAKE PROFIT
    # =========================

    print("\nSTEP 2 - TAKE PROFIT")


    result.position.current_price = (
        result.position.take_profit
    )


    result = controller.run_cycle()


    print(
        "DECISION:",
        result.decision
    )


    assert (
        result.decision["decision"]
        ==
        "CLOSE"
    )



    # =========================
    # STEP 3: VERIFY CLOSED
    # =========================

    print("\nSTEP 3 - CLOSED")


    print(
        "POSITION:",
        result.position
    )


    assert result.position is None



    print(
        "\nFULL_TRADE_LIFECYCLE_TEST_PASS"
    )



if __name__ == "__main__":

    main()