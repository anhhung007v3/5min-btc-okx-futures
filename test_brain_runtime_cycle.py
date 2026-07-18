"""
Trading Brain SHD

Brain Runtime Cycle Test V1

Test:
- RuntimeController
- BrainLoop
- MarketEngine
- DecisionEngine
- RiskEngine
- Monitor
"""


from brain.runtime.runtime_controller import RuntimeController


def main():

    print(
        "START BRAIN RUNTIME CYCLE TEST"
    )


    controller = RuntimeController()


    print(
        "STARTUP"
    )

    controller.startup()


    print(
        "RUN CYCLE"
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


    print(
        "EXECUTION:",
        context.execution_result
    )


    controller.shutdown()


    print(
        "BRAIN_RUNTIME_CYCLE_TEST_PASS"
    )



if __name__ == "__main__":
    main()