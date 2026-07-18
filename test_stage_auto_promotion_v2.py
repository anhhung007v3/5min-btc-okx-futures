from brain.position.stage_engine import Stage
from brain.position.position_manager import PositionManager
from brain.risk.capital_manager import CapitalManager



def main():

    print("START STAGE AUTO PROMOTION V2 TEST")


    capital_manager = CapitalManager(
        total_capital=20
    )


    manager = PositionManager(
        capital_manager
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


    print("OPEN:", result)

    print("STAGE:", manager.position.stage)



    print("\nSTAGE 0 -> STAGE 1")


    manager.update_stage(

        movement_ok=True,

        protection_ok=True,

        profit_percent=0

    )


    print(
        "STAGE:",
        manager.position.stage
    )


    assert (
        manager.position.stage
        ==
        Stage.STAGE_1
    )



    print("\nSTAGE 1 -> STAGE 2")


    manager.update_stage(

        movement_ok=True,

        protection_ok=True,

        profit_percent=2.5

    )


    print(
        "STAGE:",
        manager.position.stage
    )


    assert (
        manager.position.stage
        ==
        Stage.STAGE_2
    )



    print("\nSTAGE 2 -> STAGE 3")


    manager.update_stage(

        movement_ok=True,

        protection_ok=True,

        profit_percent=5.5

    )


    print(
        "STAGE:",
        manager.position.stage
    )


    assert (
        manager.position.stage
        ==
        Stage.STAGE_3
    )



    print(
        "\nSTAGE_AUTO_PROMOTION_V2_TEST_PASS"
    )



if __name__ == "__main__":

    main()