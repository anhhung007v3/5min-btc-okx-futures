"""
Trading Brain SHD
Main Runtime V2

Real runtime entry point.
"""


from brain.runtime.runtime_controller import RuntimeController
from brain.runtime.runtime_service import RuntimeService
from brain.scheduler.runtime_scheduler import RuntimeScheduler



def main():

    controller = RuntimeController()


    scheduler = RuntimeScheduler(
        controller,
        interval_seconds=5
    )


    service = RuntimeService(
        scheduler,
        controller
    )


    print(
        "SERVICE STATUS:",
        service.status()
    )


    service.start()



if __name__ == "__main__":
    main()