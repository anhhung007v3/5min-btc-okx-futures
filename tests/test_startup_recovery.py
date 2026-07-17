"""
Trading Brain SHD
Startup Recovery Test
"""

from brain.common.startup_recovery import StartupRecoveryEngine


class FakeSnapshotEngine:

    def load_snapshot(self):

        return {
            "position": {
                "side": "LONG",
                "price": 65000,
                "size": 0.001
            },
            "stage": 2
        }



class FakeReplayEngine:

    def __init__(self):

        self.called = False


    def rebuild(self):

        self.called = True



def main():

    print("===== TEST STARTUP RECOVERY V1 =====")


    snapshot_engine = FakeSnapshotEngine()

    replay_engine = FakeReplayEngine()


    recovery = StartupRecoveryEngine(
        snapshot_engine,
        replay_engine
    )


    state = recovery.recover()


    print("RECOVERED STATE:")
    print(state)


    print("REPLAY CALLED:")
    print(replay_engine.called)



if __name__ == "__main__":
    main()