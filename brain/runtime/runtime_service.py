"""
Trading Brain SHD
Runtime Service V1B

Manage Runtime lifecycle.
"""


class RuntimeService:
    """
    Service layer quản lý vòng đời SHD runtime.
    """

    def __init__(
        self,
        scheduler,
        controller
    ):

        self.scheduler = scheduler
        self.controller = controller

        self.running = False


    def start(self):
        """
        Start SHD runtime.

        Flow:

        Recovery
            |
        Scheduler
        """

        if self.running:
            return


        # Restore Brain state

        self.controller.startup()


        # Start runtime loop

        self.running = True

        self.scheduler.start()



    def stop(self):
        """
        Stop SHD runtime.
        """

        if not self.running:
            return


        self.scheduler.stop()

        self.running = False



    def status(self):
        """
        Return service status.
        """

        return (
            "RUNNING"
            if self.running
            else "STOPPED"
        )