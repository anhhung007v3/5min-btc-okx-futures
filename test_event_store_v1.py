from brain.common.event_store import (
    EventStore
)

from brain.monitor.monitor_event import (
    MonitorEvent
)



def main():

    print(
        "START EVENT STORE V1 TEST"
    )


    store = EventStore(
        "test_event_history.json"
    )


    store.clear_events()



    print(
        "\nSAVE EVENT"
    )


    event = MonitorEvent(

        event_type="TEST_EVENT",

        message="EVENT_STORE_TEST",

        timestamp="2026-07-18",

        data={

            "value": 123

        }

    )


    store.save_event(
        event
    )



    print(
        "EVENT COUNT:",
        store.count_events()
    )



    print(
        "\nLOAD EVENTS"
    )


    events = store.load_events()


    print(
        events
    )



    assert len(events) == 1

    assert events[0]["event_type"] == "TEST_EVENT"



    print(
        "\nEVENT_STORE_V1_TEST_PASS"
    )



if __name__ == "__main__":

    main()