"""
Trading Brain SHD
Runtime Service V1

Manage Runtime lifecycle.
"""


class RuntimeService:
    """
    Service layer quản lý vòng đời SHD runtime.
    """

    def __init__(
        self,
        scheduler
    ):
        self.scheduler = scheduler
        self.running = False


    def start(self):
        """
        Start SHD runtime.
        """

        if self.running:
            return

        self.running = True

        self.scheduler.start()



    def stop(self):
        """
        Stop SHD runtime.
        """

        if not self.running:
            return

        self.running = False

        self.scheduler.stop()



    def status(self):
        """
        Return service status.
        """

        return (
            "RUNNING"
            if self.running
            else "STOPPED"
        )