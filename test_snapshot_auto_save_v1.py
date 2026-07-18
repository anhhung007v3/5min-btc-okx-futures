from brain.common.snapshot_engine import (
    SnapshotEngine
)

from brain.common.position_snapshot import (
    PositionSnapshot
)

from brain.position.position_manager import (
    PositionManager
)

from brain.risk.capital_manager import (
    CapitalManager
)

from brain.position.stage_engine import (
    Stage
)



def main():

    print(
        "START SNAPSHOT AUTO SAVE V1 TEST"
    )


    snapshot_engine = SnapshotEngine(
        "test_auto_snapshot.json"
    )


    capital_manager = CapitalManager(
        total_capital=20
    )


    position_manager = PositionManager(

        capital_manager,

        snapshot_engine

    )



    print(
        "\nOPEN POSITION"
    )


    result = position_manager.open_position(

        side="LONG",

        price=62500,

        size=0.001,

        capital=5,

        stop_loss=62000,

        take_profit=63500

    )


    print(
        "OPEN:",
        result
    )


    snapshot = snapshot_engine.load_snapshot()


    print(
        "SNAPSHOT:",
        snapshot
    )



    assert snapshot["side"] == "LONG"

    assert snapshot["stage"] == "STAGE_0"



    print(
        "\nUPDATE PRICE"
    )


    position_manager.update_price(
        63500
    )


    snapshot = snapshot_engine.load_snapshot()


    print(
        "SNAPSHOT:",
        snapshot
    )


    assert snapshot["current_price"] == 63500



    print(
        "\nCLOSE POSITION"
    )


    position_manager.close_position()


    snapshot = snapshot_engine.load_snapshot()


    print(
        "SNAPSHOT:",
        snapshot
    )


    assert snapshot is None



    print(
        "\nSNAPSHOT_AUTO_SAVE_V1_TEST_PASS"
    )



if __name__ == "__main__":

    main()