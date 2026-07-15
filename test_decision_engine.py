from brain.decision.decision_engine import (
    DecisionEngine
)

from brain.market.market_state import (
    MarketState
)

from brain.position.position_state import (
    PositionState
)

from brain.position.stage_engine import (
    Stage
)



def main():

    print("===== SHD DECISION ENGINE TEST =====")


    engine = DecisionEngine()



    market = MarketState(
        movement_ok=True
    )



    print("\n1. NO POSITION")


    result = engine.evaluate(
        position=None,
        market_state=market
    )


    print(result)



    print("\n2. STAGE 0")


    position = PositionState(
        side="LONG",
        stage=Stage.STAGE_0
    )


    result = engine.evaluate(
        position=position,
        market_state=market
    )


    print(result)



    print("\n3. STAGE 1")


    position.stage = Stage.STAGE_1


    result = engine.evaluate(
        position=position,
        market_state=market
    )


    print(result)



    print("\n4. STAGE 2")


    position.stage = Stage.STAGE_2


    result = engine.evaluate(
        position=position,
        market_state=market
    )


    print(result)



if __name__ == "__main__":
    main()