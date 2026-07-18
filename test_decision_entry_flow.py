"""
Trading Brain SHD

Decision Entry Flow V1 Test
"""


from brain.decision.decision_engine import (
    DecisionEngine
)



class FakeMarketState:

    movement_ok = True



def main():

    print(
        "START DECISION ENTRY FLOW TEST"
    )


    engine = DecisionEngine()


    market_state = FakeMarketState()


    entry_signal = {

        "signal": "LONG_READY",

        "confidence": 0.8

    }


    result = engine.evaluate(

        position=None,

        market_state=market_state,

        entry_signal=entry_signal

    )


    print(
        "DECISION:",
        result
    )


    assert result["decision"] == "OPEN"

    assert result["reason"] == "LONG_READY"


    print(
        "DECISION_ENTRY_FLOW_TEST_PASS"
    )



if __name__ == "__main__":

    main()