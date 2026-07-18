from brain.runtime.runtime_controller import RuntimeController


def main():
    controller = RuntimeController()

    print("Runtime Controller created.")

    print("STARTUP...")
    controller.startup()

    print("RUN ONE CYCLE...")
    controller.run_cycle()

    print("SHUTDOWN...")
    controller.shutdown()

    print("RUNTIME_CONTROLLER_TEST_PASS")


if __name__ == "__main__":
    main()