"""
Trading Brain SHD
BrainMonitor EventStore Integration Test
"""


from brain.monitor.brain_monitor import BrainMonitor
from brain.monitor.monitor_event import MonitorEvent
from brain.common.event_store import EventStore



def main():

    print("===== TEST BRAIN MONITOR EVENT STORE V1 =====")


    store = EventStore(
        "test_brain_history.json"
    )


    monitor = BrainMonitor(
        event_store=store
    )


    event = MonitorEvent(

        event_type="TEST_EVENT",

        message="MEMORY_SAVE_OK",

        timestamp="2026-07-17"

    )


    monitor.record(
        event
    )


    events = store.load_events()


    print("EVENT COUNT:")
    print(len(events))


    print("LAST EVENT:")
    print(events[-1])



if __name__ == "__main__":

    main()