"""
Trading Brain SHD

Entry Signal Engine V1 Test
"""


from brain.decision.entry_signal_engine import (
    EntrySignalEngine
)



class FakeMarketState:
    """
    Fake market data for testing.
    """

    direction = "NONE"

    trend_strength = 0.8

    volatility = 0.5

    movement_ok = True



def main():

    print(
        "START ENTRY SIGNAL TEST"
    )


    engine = EntrySignalEngine()


    market_state = FakeMarketState()


    result = engine.evaluate(
        market_state
    )


    print(
        "SIGNAL:",
        result
    )


    assert result["signal"] == "LONG_READY"


    assert result["confidence"] == 0.8


    print(
        "ENTRY_SIGNAL_ENGINE_TEST_PASS"
    )



if __name__ == "__main__":

    main()