from brain.risk.risk_engine import RiskEngine
from brain.position.position_state import PositionState


def main():

    print("START PROFIT TRACKING TEST")


    risk = RiskEngine()


    position = PositionState(
        side="LONG"
    )


    position.entry_price = 62500

    position.current_price = 63500



    profit = risk.calculate_profit_percent(

        side=position.side,

        entry_price=position.entry_price,

        current_price=position.current_price

    )


    print("ENTRY:", position.entry_price)

    print("CURRENT:", position.current_price)

    print("PROFIT:", profit, "%")



    assert round(profit, 2) == 1.60



    print(
        "PROFIT_TRACKING_TEST_PASS"
    )



if __name__ == "__main__":

    main()