"""
Trading Brain SHD
Runtime Entry Point V1
"""


from brain.runtime.runtime_service import RuntimeService
from brain.scheduler.runtime_scheduler import RuntimeScheduler


class DummyController:
    """
    Temporary controller adapter.

    RuntimeController sẽ được inject thật sau.
    """

    def startup(self):
        print("SHD STARTUP")


    def run_cycle(self):
        print("SHD CYCLE")


    def shutdown(self):
        print("SHD SHUTDOWN")



def main():

    controller = DummyController()


    scheduler = RuntimeScheduler(
        controller,
        interval_seconds=5
    )


    service = RuntimeService(
        scheduler
    )


    print(
        "SERVICE STATUS:",
        service.status()
    )


    service.start()



if __name__ == "__main__":
    main()