"""
Trading Brain SHD
Main Runtime V3

Real runtime entry point.
"""

import time


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


    try:

        service.start()


        while True:

            time.sleep(1)


    except KeyboardInterrupt:

        print(
            "STOP REQUEST"
        )

        service.stop()



if __name__ == "__main__":
    main()