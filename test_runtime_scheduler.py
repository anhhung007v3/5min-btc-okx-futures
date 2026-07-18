from brain.scheduler.runtime_scheduler import RuntimeScheduler


class DummyController:

    def startup(self):
        print("STARTUP")

    def run_cycle(self):
        print("RUN CYCLE")
        scheduler.stop()

    def shutdown(self):
        print("SHUTDOWN")


scheduler = RuntimeScheduler(
    DummyController(),
    interval_seconds=1
)

scheduler.start()

print("RUNTIME_SCHEDULER_TEST_PASS")