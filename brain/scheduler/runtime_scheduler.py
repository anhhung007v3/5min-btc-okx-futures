"""
Trading Brain SHD
Runtime Scheduler V2

Run RuntimeController in background thread.
"""

import time
import threading


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
        self.thread = None



    def _run_loop(self):
        """
        Internal runtime loop.
        """

        self.controller.startup()


        while self.running:

            self.controller.run_cycle()

            time.sleep(
                self.interval_seconds
            )


        self.controller.shutdown()



    def start(self):
        """
        Start runtime scheduler.
        """

        if self.running:
            return


        self.running = True


        self.thread = threading.Thread(
            target=self._run_loop
        )


        self.thread.start()



    def stop(self):
        """
        Stop runtime scheduler.
        """

        if not self.running:
            return


        self.running = False


        current_thread = threading.current_thread()


        if (
            self.thread
            and
            self.thread != current_thread
        ):

            self.thread.join(
                timeout=5
            )


        self.thread = None