from brain.runtime.runtime_service import RuntimeService


class DummyScheduler:

    def start(self):
        print("SCHEDULER_START")

    def stop(self):
        print("SCHEDULER_STOP")



def main():

    scheduler = DummyScheduler()

    service = RuntimeService(
        scheduler
    )

    print(service.status())

    service.start()

    print(service.status())

    service.stop()

    print(service.status())



    print("RUNTIME_SERVICE_TEST_PASS")


if __name__ == "__main__":
    main()
