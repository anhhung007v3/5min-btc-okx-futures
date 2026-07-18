from brain.runtime.runtime_controller import (
    RuntimeController
)

from brain.common.position_snapshot import (
    PositionSnapshot
)

from brain.position.position_state import (
    PositionState
)

from brain.position.stage_engine import (
    Stage
)



def main():

    print("START RUNTIME POSITION RESTORE V1 TEST")


    controller = RuntimeController()


    print("\nCREATE SNAPSHOT")


    position = PositionState(

        side="LONG",

        stage=Stage.STAGE_2

    )


    position.add_entry(

        price=62500,

        size=0.001,

        capital=5

    )


    snapshot = PositionSnapshot.to_dict(
        position
    )


    controller.snapshot_engine.save_snapshot(
        snapshot
    )


    print(
        "SNAPSHOT SAVED:",
        snapshot
    )



    print("\nSTARTUP RECOVERY")


    result = controller.startup()


    print(
        "RECOVERY RESULT:",
        result
    )



    print(
        "\nCURRENT POSITION:"
    )


    print(
        controller.position_manager.position
    )


    assert result is not None


    print(
        "\nRUNTIME_POSITION_RESTORE_V1_TEST_PASS"
    )



if __name__ == "__main__":

    main()