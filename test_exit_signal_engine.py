from brain.risk.exit_signal_engine import (
    ExitSignalEngine
)


from brain.position.position_state import (
    PositionState
)


from brain.position.stage_engine import (
    Stage
)



def main():

    print("START EXIT SIGNAL TEST")


    engine = ExitSignalEngine()



    # CREATE LONG POSITION

    position = PositionState(

        side="LONG",

        stage=Stage.STAGE_0

    )


    position.entry_price = 62500

    position.stop_loss = 62000

    position.take_profit = 63500



    # TEST TAKE PROFIT

    result = engine.evaluate(

        position,

        current_price=63500

    )


    print(
        "TAKE PROFIT RESULT:",
        result
    )


    assert result["exit"] == True

    assert result["reason"] == "TAKE_PROFIT"



    # TEST STOP LOSS

    result = engine.evaluate(

        position,

        current_price=62000

    )


    print(
        "STOP LOSS RESULT:",
        result
    )


    assert result["exit"] == True

    assert result["reason"] == "STOP_LOSS"



    # TEST HOLD

    result = engine.evaluate(

        position,

        current_price=62500

    )


    print(
        "HOLD RESULT:",
        result
    )


    assert result["exit"] == False

    assert result["reason"] == "HOLD"



    print(
        "EXIT_SIGNAL_ENGINE_TEST_PASS"
    )



if __name__ == "__main__":

    main()