from brain.position.position_state import (
    PositionState
)

from brain.position.stage_engine import (
    Stage
)

from brain.common.position_snapshot import (
    PositionSnapshot
)



def main():

    print("START POSITION SNAPSHOT V1 TEST")


    print("\nCREATE POSITION")


    position = PositionState(

        side="LONG",

        stage=Stage.STAGE_2

    )


    position.add_entry(

        price=62500,

        size=0.001,

        capital=5

    )


    position.current_price = 63500

    position.set_risk(

        stop_loss=62500,

        take_profit=64000

    )


    print(
        "ORIGINAL:",
        position
    )



    print("\nSAVE TO DICT")


    snapshot = PositionSnapshot.to_dict(

        position

    )


    print(
        "SNAPSHOT:",
        snapshot
    )



    print("\nRESTORE POSITION")


    restored = PositionSnapshot.from_dict(

        snapshot

    )


    print(
        "RESTORED:",
        restored
    )



    assert restored.side == "LONG"

    assert restored.stage == Stage.STAGE_2

    assert restored.entry_price == 62500

    assert restored.size == 0.001

    assert restored.stop_loss == 62500

    assert restored.take_profit == 64000



    print(
        "\nPOSITION_SNAPSHOT_V1_TEST_PASS"
    )



if __name__ == "__main__":

    main()