from brain.position.position_state import (
    PositionState
)

from brain.position.stage_engine import (
    Stage
)


def main():

    print("===== SHD POSITION STATE TEST =====")


    position = PositionState(
        side="LONG",
        stage=Stage.STAGE_0
    )


    print("\nCREATE POSITION")

    print("SIDE:")
    print(position.side)

    print("STAGE:")
    print(position.stage)



    print("\nADD ENTRY 1")

    position.add_entry(
        price=65000,
        size=0.000077,
        capital=5
    )


    print("TOTAL CAPITAL:")
    print(position.total_capital)

    print("AVERAGE PRICE:")
    print(position.average_price)



    print("\nADD ENTRY 2")

    position.add_entry(
        price=65200,
        size=0.0000767,
        capital=5
    )


    print("TOTAL CAPITAL:")
    print(position.total_capital)

    print("TOTAL SIZE:")
    print(position.total_size)

    print("AVERAGE PRICE:")
    print(position.average_price)



    print("\nENTRIES:")

    for entry in position.entries:
        print(entry)



if __name__ == "__main__":
    main()