from dataclasses import dataclass
from typing import Optional



@dataclass
class MonitorEvent:
    """
    Sự kiện được ghi nhận bởi Monitor Layer SHD.

    Ví dụ:

    - MARKET_UPDATE
    - DECISION_MADE
    - RISK_CHECK
    - EXECUTION_RESULT


    Monitor chỉ ghi nhận.
    Không thay đổi hệ thống.
    """


    event_type: str


    message: str


    timestamp: str


    data: Optional[dict] = None