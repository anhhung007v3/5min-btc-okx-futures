from brain.common.snapshot_engine import SnapshotEngine
from brain.common.position_snapshot import PositionSnapshot
from brain.position.position_state import PositionState
from brain.position.stage_engine import Stage



def main():

    print("START STARTUP RECOVERY V1 TEST")


    position = PositionState(

        side="LONG",

        stage=Stage.STAGE_2

    )


    position.add_entry(

        price=62500,

        size=0.001,

        capital=5

    )


    snapshot_data = PositionSnapshot.to_dict(
        position
    )


    engine = SnapshotEngine(
        "test_brain_snapshot.json"
    )


    engine.save_snapshot(
        snapshot_data
    )


    loaded = engine.load_snapshot()


    restored = PositionSnapshot.from_dict(
        loaded
    )


    print("LOADED:", loaded)

    print("RESTORED:", restored)


    assert restored.side == "LONG"

    assert restored.stage == Stage.STAGE_2


    print(
        "STARTUP_RECOVERY_V1_TEST_PASS"
    )



if __name__ == "__main__":

    main()