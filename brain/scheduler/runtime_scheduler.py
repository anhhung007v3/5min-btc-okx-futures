"""
Trading Brain SHD
Runtime Scheduler V1

Run RuntimeController continuously.
"""

import time


class RuntimeScheduler:
    """
    Runtime loop for Trading Brain.
    """

    def __init__(
        self,
        controller,
        interval_seconds=5
    ):
        self.controller = controller
        self.interval_seconds = interval_seconds
        self.running = False

    def start(self):
        """
        Start runtime loop.
        """
        self.running = True

        self.controller.startup()

        while self.running:
            self.controller.run_cycle()
            time.sleep(self.interval_seconds)

    def stop(self):
        """
        Stop runtime loop.
        """
        self.running = False

        self.controller.shutdown()