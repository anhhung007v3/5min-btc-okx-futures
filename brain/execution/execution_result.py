from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class ExecutionResult:
    """
    Kết quả sau khi Execution Layer thực hiện hành động.

    Execution chỉ báo cáo kết quả.

    Không:
    - Quyết định giao dịch.
    - Phân tích thị trường.
    - Tính Risk.
    """


    success: bool


    action: str


    message: str


    timestamp: str


    order_id: Optional[str] = None