from typing import Dict


def calculate_position_size(
    balance: float,
    risk_percent: float,
    entry_price: float,
    stop_loss: float
) -> Dict:
    """
    Tính khối lượng BTC dựa trên % rủi ro tài khoản.

    balance:
        Số dư USDT

    risk_percent:
        % rủi ro mỗi lệnh
        Ví dụ: 1 = 1%

    entry_price:
        Giá vào lệnh

    stop_loss:
        Giá SL
    """


    risk_amount = balance * (risk_percent / 100)


    stop_distance = abs(
        entry_price - stop_loss
    )


    if stop_distance == 0:

        return {
            "error": "INVALID_STOP_DISTANCE"
        }


    btc_size = risk_amount / stop_distance


    return {

        "balance": balance,

        "risk_percent": risk_percent,

        "risk_amount": round(
            risk_amount,
            2
        ),

        "entry_price": entry_price,

        "stop_loss": stop_loss,

        "stop_distance": round(
            stop_distance,
            2
        ),

        "btc_size": round(
            btc_size,
            6
        )

    }



if __name__ == "__main__":


    print("===== POSITION SIZE TEST =====")


    result = calculate_position_size(

        balance=1000,

        risk_percent=1,

        entry_price=62800,

        stop_loss=62980

    )


    print(result)