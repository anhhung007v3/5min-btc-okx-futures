from dataclasses import dataclass, field
from typing import List, Dict, Optional

from brain.position.stage_engine import Stage


@dataclass
class PositionState:
    """
    Hồ sơ của một chu kỳ giao dịch SHD.

    Một Position có thể có nhiều Entry.

    Chỉ lưu trạng thái.
    """


    side: str


    stage: Stage = Stage.STAGE_0


    entries: List[Dict] = field(
        default_factory=list
    )


    total_capital: float = 0.0


    total_size: float = 0.0


    average_price: Optional[float] = None


    # ===== RISK DATA =====

    stop_loss: Optional[float] = None


    take_profit: Optional[float] = None


    trailing_stop: Optional[float] = None



    def add_entry(
        self,
        price: float,
        size: float,
        capital: float
    ):
        """
        Thêm Entry vào Position.
        """


        self.entries.append(
            {
                "price": price,
                "size": size,
                "capital": capital
            }
        )


        self.total_size += size


        self.total_capital += capital


        self.calculate_average_price()



    def calculate_average_price(self):
        """
        Tính giá vốn trung bình theo BTC size.
        """


        if self.total_size <= 0:

            self.average_price = None

            return


        total_value = 0.0


        for entry in self.entries:

            total_value += (
                entry["price"]
                *
                entry["size"]
            )


        self.average_price = (
            total_value
            /
            self.total_size
        )



    def set_risk(
        self,
        stop_loss: float,
        take_profit: float
    ):
        """
        Cập nhật vùng bảo vệ Position.
        """


        self.stop_loss = stop_loss


        self.take_profit = take_profit