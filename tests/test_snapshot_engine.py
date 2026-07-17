"""
Trading Brain SHD
Snapshot Engine Test
"""

from brain.common.snapshot_engine import SnapshotEngine


def main():

    print("===== TEST SNAPSHOT ENGINE V1 =====")


    snapshot = SnapshotEngine(
        "test_snapshot.json"
    )


    state = {
        "position": {
            "side": "LONG",
            "price": 65000,
            "size": 0.001
        },
        "stage": 2
    }


    snapshot.save_snapshot(
        state
    )


    loaded = snapshot.load_snapshot()


    print("SNAPSHOT:")
    print(loaded)



if __name__ == "__main__":
    main()