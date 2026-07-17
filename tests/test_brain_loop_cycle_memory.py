"""
Trading Brain SHD
BrainLoop Cycle Memory Test
"""


from brain.brain_loop import BrainLoop
from brain.common.brain_context import BrainContext
from brain.monitor.monitor_event import MonitorEvent



class FakeMarket:

    def evaluate(
        self,
        trend_strength,
        volatility
    ):

        return {
            "market": "GOOD"
        }



class FakeDecision:

    def evaluate(
        self,
        position,
        market_state
    ):

        return {
            "decision": "WAIT"
        }



class FakeRisk:

    def check_protection(
        self,
        position
    ):

        return True



class FakeExecution:

    def open_position(
        self,
        **kwargs
    ):

        return None



class FakeMonitor:

    def __init__(self):

        self.events = []


    def record(
        self,
        event
    ):

        self.events.append(
            event
        )



def main():

    print(
        "===== TEST BRAIN LOOP CYCLE MEMORY V1 ====="
    )


    monitor = FakeMonitor()


    brain = BrainLoop(

        FakeMarket(),

        FakeDecision(),

        FakeRisk(),

        FakeExecution(),

        monitor

    )


    context = BrainContext()


    brain.run(
        context
    )


    print(
        "EVENT COUNT:"
    )

    print(
        len(monitor.events)
    )


    for event in monitor.events:

        print(
            event.event_type
        )



if __name__ == "__main__":

    main()