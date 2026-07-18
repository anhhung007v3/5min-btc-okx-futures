from brain.common.event_store import (
    EventStore
)

from brain.monitor.brain_monitor import (
    BrainMonitor
)

from brain.monitor.monitor_event import (
    MonitorEvent
)



def main():

    print(
        "START MONITOR EVENT STORE V1 TEST"
    )


    store = EventStore(
        "test_monitor_history.json"
    )


    store.clear_events()



    monitor = BrainMonitor(
        event_store=store
    )



    print(
        "\nSEND EVENT"
    )


    event = MonitorEvent(

        event_type="MONITOR_TEST",

        message="BRAIN_MONITOR_CONNECTED",

        timestamp="2026-07-18",

        data={

            "status": "OK"

        }

    )


    monitor.record(
        event
    )



    print(
        "\nMEMORY EVENTS:"
    )

    print(
        len(
            monitor.get_events()
        )
    )



    print(
        "\nSTORE EVENTS:"
    )

    events = store.load_events()

    print(
        events
    )



    assert len(
        monitor.get_events()
    ) == 1


    assert len(events) == 1


    assert events[0]["event_type"] == "MONITOR_TEST"



    print(
        "\nMONITOR_EVENT_STORE_V1_TEST_PASS"
    )



if __name__ == "__main__":

    main()