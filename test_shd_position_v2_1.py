from brain.risk.capital_manager import (
    CapitalManager
)

from brain.position.position_manager import (
    PositionManager
)

from brain.position.stage_engine import (
    Stage
)


def main():

    print("===== SHD POSITION MANAGER V2.1 TEST =====")


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
        capital=5,
        stop_loss=64800,
        take_profit=65400
    )


    print("RESULT:")
    print(result)


    print("\nPOSITION:")

    print(manager.position)



    print("\nRISK DATA:")

    print(
        "STOP LOSS:",
        manager.position.stop_loss
    )


    print(
        "TAKE PROFIT:",
        manager.position.take_profit
    )



    print("\nSTAGE:")

    print(
        manager.position.stage
    )



    print("\n2. MOVE STOP TO SAFE")


    manager.position.stop_loss = 65100


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



    print("\nFINAL POSITION")

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