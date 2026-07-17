"""
Trading Brain SHD
Startup Recovery Engine

Restore Brain state from snapshot and replay events.
"""


class StartupRecoveryEngine:
    """
    Coordinate startup recovery flow.

    Flow:

    Snapshot
        |
        v
    Restore State
        |
        v
    Replay Events
        |
        v
    Ready Brain
    """


    def __init__(
        self,
        snapshot_engine,
        replay_engine
    ):

        self.snapshot_engine = snapshot_engine
        self.replay_engine = replay_engine



    def recover(self):

        snapshot = (
            self.snapshot_engine
            .load_snapshot()
        )


        self.replay_engine.rebuild()


        return snapshot