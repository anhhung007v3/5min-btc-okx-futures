from datetime import datetime


from brain.monitor.monitor_event import (
    MonitorEvent
)


from brain.monitor.brain_monitor import (
    BrainMonitor
)



def main():

    print(
        "===== TEST MONITOR V1 ====="
    )


    monitor = BrainMonitor(
        log_file="test_brain_monitor.log"
    )


    event = MonitorEvent(

        event_type="DECISION_MADE",

        message="WAIT_PROTECTION",

        timestamp=datetime.utcnow().isoformat(),

        data={

            "stage": "STAGE_0",

            "reason": "POSITION_NOT_SAFE"

        }

    )



    monitor.record(
        event
    )



    events = monitor.get_events()



    print(
        "EVENT COUNT:",
        len(events)
    )


    print(
        "LAST EVENT:",
        events[-1].event_type
    )


    print(
        "MESSAGE:",
        events[-1].message
    )



if __name__ == "__main__":

    main()
