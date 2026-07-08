from typing import Dict


def calculate_risk(
    side: str,
    entry_price: float,
    atr: float,
    sl_atr_multiplier: float = 1.5,
    risk_reward: float = 2.0
) -> Dict:
    """
    Tính Stop Loss và Take Profit theo ATR.

    side:
        LONG
        SHORT
    """

    if side == "LONG":

        stop_loss = entry_price - (atr * sl_atr_multiplier)

        risk = entry_price - stop_loss

        take_profit = entry_price + (risk * risk_reward)


    elif side == "SHORT":

        stop_loss = entry_price + (atr * sl_atr_multiplier)

        risk = stop_loss - entry_price

        take_profit = entry_price - (risk * risk_reward)


    else:

        return {
            "error": "INVALID_SIDE"
        }


    return {

        "side": side,

        "entry_price": round(entry_price, 2),

        "stop_loss": round(stop_loss, 2),

        "take_profit": round(take_profit, 2),

        "risk_reward": risk_reward,

        "atr": round(atr, 2)

    }



if __name__ == "__main__":


    print("===== RISK MANAGER TEST =====")


    long_test = calculate_risk(
        "LONG",
        62700,
        100
    )


    short_test = calculate_risk(
        "SHORT",
        62700,
        100
    )


    print(long_test)

    print(short_test)