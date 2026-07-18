"""
Trading Brain SHD

Brain Runtime Cycle V2

Inject market context.
"""


from brain.runtime.runtime_controller import RuntimeController



def main():

    print(
        "START BRAIN RUNTIME CYCLE V2 TEST"
    )


    controller = RuntimeController()


    print(
        "STARTUP"
    )

    controller.startup()


    # Inject fake market data

    controller.context.trend_strength = 0.8

    controller.context.volatility = 0.6


    print(
        "RUN CYCLE WITH MARKET DATA"
    )


    context = controller.run_cycle()


    print(
        "MARKET STATE:",
        context.market_state
    )


    print(
        "DECISION:",
        context.decision
    )


    print(
        "PROTECTION:",
        context.protection_ok
    )


    controller.shutdown()


    print(
        "BRAIN_RUNTIME_CYCLE_V2_TEST_PASS"
    )



if __name__ == "__main__":
    main()