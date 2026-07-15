from brain.risk.risk_engine import (
    RiskEngine
)


def main():

    print("===== SHD RISK ENGINE TEST =====")


    risk = RiskEngine()



    print("\n1. LONG NOT SAFE")


    result = risk.check_protection(
        side="LONG",
        entry_price=65000,
        current_price=65300,
        stop_loss=64800
    )


    print("RESULT:")
    print(result)



    print("\n2. LONG SAFE")


    result = risk.check_protection(
        side="LONG",
        entry_price=65000,
        current_price=65300,
        stop_loss=65100
    )


    print("RESULT:")
    print(result)



    print("\n3. SHORT NOT SAFE")


    result = risk.check_protection(
        side="SHORT",
        entry_price=65000,
        current_price=64700,
        stop_loss=65200
    )


    print("RESULT:")
    print(result)



    print("\n4. SHORT SAFE")


    result = risk.check_protection(
        side="SHORT",
        entry_price=65000,
        current_price=64700,
        stop_loss=64900
    )


    print("RESULT:")
    print(result)



    print("\n5. PROFIT CHECK")


    profit = risk.calculate_profit_percent(
        side="LONG",
        entry_price=65000,
        current_price=65300
    )


    print("LONG PROFIT %:")
    print(profit)



if __name__ == "__main__":
    main()