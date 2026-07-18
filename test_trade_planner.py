from brain.decision.trade_planner import TradePlanner


def main():

    planner = TradePlanner()


    signal = {

        "signal": "LONG_READY",

        "confidence": 0.8

    }


    plan = planner.create_plan(

        signal,

        62500

    )


    print(plan)


    assert plan["side"] == "LONG"

    print(
        "TRADE_PLANNER_TEST_PASS"
    )



if __name__ == "__main__":
    main()