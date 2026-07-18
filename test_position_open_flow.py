from brain.position.position_manager import PositionManager
from brain.risk.capital_manager import CapitalManager


def main():

    print("START POSITION OPEN FLOW TEST")


    capital = CapitalManager(
        total_capital=20
    )


    manager = PositionManager(
        capital
    )


    result = manager.open_position(

        side="LONG",

        price=62500,

        size=0.001,

        capital=5,

        stop_loss=62000,

        take_profit=63500

    )


    print(
        "OPEN RESULT:",
        result
    )


    print(
        "POSITION:",
        manager.position
    )


    assert result is True

    assert manager.position is not None

    assert manager.position.side == "LONG"


    print(
        "POSITION_OPEN_FLOW_TEST_PASS"
    )



if __name__ == "__main__":
    main()