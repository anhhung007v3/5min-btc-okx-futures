from brain.decision.decision_engine import (
    DecisionEngine
)

from brain.position.position_state import (
    PositionState
)

from brain.position.stage_engine import (
    Stage
)


def main():

    print("START DECISION EXIT FLOW TEST")


    engine = DecisionEngine()



    position = PositionState(

        side="LONG",

        stage=Stage.STAGE_0

    )



    position.entry_price = 62500



    market_state = type(
        "MarketState",
        (),
        {
            "movement_ok": True
        }
    )()



    exit_signal = {

        "exit": True,

        "reason": "TAKE_PROFIT"

    }



    result = engine.evaluate(

        position=position,

        market_state=market_state,

        exit_signal=exit_signal

    )


    print(
        "DECISION:",
        result
    )


    assert result["decision"] == "CLOSE"

    assert result["reason"] == "TAKE_PROFIT"



    print(
        "DECISION_EXIT_FLOW_TEST_PASS"
    )



if __name__ == "__main__":

    main()