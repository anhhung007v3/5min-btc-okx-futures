from brain.runtime.runtime_service import RuntimeService


class MockScheduler:

    def __init__(self):
        self.running = False


    def start(self):
        self.running = True
        print("SCHEDULER_START")


    def stop(self):
        self.running = False
        print("SCHEDULER_STOP")



class MockController:

    def startup(self):
        print("RECOVERY_START")



def main():

    scheduler = MockScheduler()

    controller = MockController()


    service = RuntimeService(
        scheduler,
        controller
    )


    print(service.status())


    service.start()

    print(service.status())


    service.stop()

    print(service.status())


    print("RUNTIME_SERVICE_BOOT_TEST_PASS")



if __name__ == "__main__":
    main()