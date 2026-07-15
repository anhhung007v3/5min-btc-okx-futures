from brain.risk.capital_manager import (
    CapitalManager
)

from brain.position.position_manager import (
    PositionManager
)


def main():

    print("===== SHD POSITION LIFE CYCLE TEST =====")


    capital = CapitalManager(
        total_capital=20
    )


    position = PositionManager(
        capital_manager=capital
    )


    print("\nTOTAL CAPITAL:")
    print(capital.total_capital)


    print("\nMAX USAGE:")
    print(capital.max_capital())


    print("\n1. OPEN FIRST POSITION 5 USDT")

    result = position.open_position(
        5
    )

    print("RESULT:")
    print(result)

    print("USED CAPITAL:")
    print(capital.used_capital)

    print("STAGE:")
    print(position.stage)



    print("\n2. TRY ADD POSITION BEFORE SAFE")

    result = position.add_position(
        5
    )

    print("RESULT:")
    print(result)

    print("USED CAPITAL:")
    print(capital.used_capital)



    print("\n3. MARKET MOVES + PROTECTION OK")

    stage = position.update_stage(
        movement_ok=True,
        protection_ok=True
    )

    print("NEW STAGE:")
    print(stage)



    print("\n4. ADD POSITION AFTER STAGE 1")

    result = position.add_position(
        5
    )

    print("RESULT:")
    print(result)

    print("USED CAPITAL:")
    print(capital.used_capital)



    print("\n5. FINAL STATUS")

    print("STAGE:")
    print(position.stage)

    print("AVAILABLE CAPITAL:")
    print(capital.available_capital())



if __name__ == "__main__":
    main()