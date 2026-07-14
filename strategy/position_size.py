from typing import Dict
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))
import config


def calculate_position_size(
    balance: float,
    risk_percent: float,
    entry_price: float,
    stop_loss: float
) -> Dict:
    """
    Tính khối lượng BTC theo % rủi ro.

    Phiên bản V2:
    - Giữ tương thích với code cũ.
    - Bổ sung Notional Value.
    - Bổ sung Margin Used.
    - Chưa giới hạn Margin (sẽ bật ở bước kế tiếp).
    """

    risk_amount = balance * (risk_percent / 100)

    stop_distance = abs(entry_price - stop_loss)

    if stop_distance == 0:
        return {
            "error": "INVALID_STOP_DISTANCE"
        }

    btc_size = risk_amount / stop_distance

    notional_value = btc_size * entry_price

    leverage = config.LEVERAGE

    margin_used = notional_value / leverage

    if margin_used > config.MAX_MARGIN_PER_TRADE:

        margin_used = config.MAX_MARGIN_PER_TRADE

        notional_value = margin_used * leverage

        btc_size = notional_value / entry_price

    return {

        "balance": round(balance, 2),

        "risk_percent": risk_percent,

        "risk_amount": round(risk_amount, 2),

        "entry_price": entry_price,

        "stop_loss": stop_loss,

        "stop_distance": round(stop_distance, 2),

        "btc_size": round(btc_size, 6),

        "notional_value": round(notional_value, 2),

        "margin_used": round(margin_used, 2),

        "leverage": leverage

    }


if __name__ == "__main__":

    print("===== POSITION SIZE TEST =====")

    result = calculate_position_size(

        balance=config.ACCOUNT_SIZE,

        risk_percent=1,

        entry_price=62800,

        stop_loss=62980

    )

    print(result)