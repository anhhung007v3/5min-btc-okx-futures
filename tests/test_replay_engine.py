from brain.common.event_store import EventStore
from brain.monitor.monitor_event import MonitorEvent
from brain.projection.projection_engine import ProjectionEngine
from brain.projection.replay_engine import ReplayEngine

from datetime import datetime


def main():

    print("===== TEST REPLAY ENGINE V1 =====")

    store = EventStore(
        "test_replay_history.json"
    )

    event = MonitorEvent(
        event_type="POSITION_OPENED",
        message="OPEN LONG",
        timestamp=datetime.now().isoformat(),
        data={
            "side": "LONG",
            "price": 65000,
            "size": 0.001
        }
    )

    store.save_event(event)

    projection_engine = ProjectionEngine()

    replay = ReplayEngine(
        store,
        projection_engine
    )

    replay.rebuild()

    position = (
        projection_engine
        .get_projection("position")
        .get_position()
    )

    print("POSITION:")
    print(position)


if __name__ == "__main__":
    main()