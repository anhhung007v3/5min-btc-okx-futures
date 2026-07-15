from brain.risk.capital_manager import (
    CapitalManager
)

from brain.position.position_manager import (
    PositionManager
)


def main():

    print("===== SHD POSITION MANAGER V2 TEST =====")


    capital = CapitalManager(
        total_capital=20
    )


    manager = PositionManager(
        capital_manager=capital
    )


    print("\n1. OPEN LONG POSITION")


    result = manager.open_position(
        side="LONG",
        price=65000,
        size=0.000077,
        capital=5
    )


    print("RESULT:")
    print(result)


    print("\nPOSITION:")

    print(manager.position)



    print("\nSTAGE:")

    print(
        manager.position.stage
    )


    print("\nTOTAL CAPITAL:")

    print(
        manager.position.total_capital
    )



    print("\n2. UPDATE STAGE")


    stage = manager.update_stage(
        movement_ok=True,
        protection_ok=True
    )


    print("NEW STAGE:")

    print(stage)



    print("\n3. ADD SECOND ENTRY")


    result = manager.add_position(
        price=65200,
        size=0.0000767,
        capital=5
    )


    print("RESULT:")

    print(result)



    print("\nPOSITION DATA:")

    print(
        "ENTRIES:",
        len(manager.position.entries)
    )


    print(
        "TOTAL CAPITAL:",
        manager.position.total_capital
    )


    print(
        "AVERAGE PRICE:",
        manager.position.average_price
    )


    print(
        "USED CAPITAL:",
        capital.used_capital
    )



if __name__ == "__main__":
    main()