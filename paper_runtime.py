import time

from brain.runtime.runtime_controller import (
    RuntimeController
)



def main():

    print(
        "START SHD PAPER RUNTIME V1"
    )


    runtime = RuntimeController()



    print(
        "\nSTARTUP RECOVERY"
    )


    snapshot = runtime.startup()


    print(
        "SNAPSHOT:",
        snapshot
    )



    try:

        while True:

            print(
                "\n===== SHD CYCLE ====="
            )

   
            context = runtime.run_cycle()


            print(
                "BTC PRICE:",
                context.market_price
            )

            print(
                "POSITION:",
                context.position
            )

            print(
                "ENTRY SIGNAL:",
                context.entry_signal
            )

            print(
                "DECISION:",
                context.decision
            )


            print(
                "EXECUTION:",
                context.execution_result
            )


            print(
                "WAIT 5 MINUTES"
            )


            time.sleep(
                300
            )



    except KeyboardInterrupt:


        print(
            "\nSTOP SHD PAPER RUNTIME"
        )


        runtime.shutdown()



if __name__ == "__main__":

    main()
