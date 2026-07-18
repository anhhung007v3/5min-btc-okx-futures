from brain.position.position_manager import PositionManager
from brain.risk.capital_manager import CapitalManager
from brain.position.stage_engine import Stage


def main():

    print("START POSITION MANAGEMENT TEST")


    capital = CapitalManager(
        total_capital=20
    )


    manager = PositionManager(
        capital_manager=capital
    )


    print("\nOPEN POSITION")


    result = manager.open_position(

        side="LONG",

        price=62500,

        size=0.001,

        capital=5,

        stop_loss=62000,

        take_profit=63500

    )


    print("OPEN RESULT:", result)


    assert result is True


    print(
        "POSITION:",
        manager.position
    )


    print("\nUPDATE PRICE")


    result = manager.update_price(
        63500
    )


    print(
        "UPDATE RESULT:",
        result
    )


    print(
        "CURRENT PRICE:",
        manager.position.current_price
    )


    assert manager.position.current_price == 63500



    print("\nUPDATE STAGE")


    stage = manager.update_stage(

        movement_ok=True,

        protection_ok=True

    )


    print(
        "STAGE:",
        stage
    )


    assert stage is not None



    print(
        "\nPOSITION_MANAGEMENT_TEST_PASS"
    )



if __name__ == "__main__":

    main()