from datetime import datetime

from brain.monitor.monitor_event import (
    MonitorEvent
)

from brain.common.event_store import (
    EventStore
)


def main():

    print(
        "===== TEST EVENT STORE V1 ====="
    )


    store = EventStore(
        "test_brain_history.json"
    )


    event = MonitorEvent(

        event_type="TEST_EVENT",

        message="MEMORY_SAVE_OK",

        timestamp=datetime.now().isoformat(),

        data={
            "value": 1
        }

    )


    store.save_event(
        event
    )


    events = store.load_events()


    print(
        "EVENT COUNT:",
        len(events)
    )


    print(
        "LAST EVENT:"
    )

    print(
        events[-1]
    )



if __name__ == "__main__":

    main()