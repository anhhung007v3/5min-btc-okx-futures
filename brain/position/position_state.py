from dataclasses import dataclass, field

from brain.position.stage_engine import Stage



@dataclass
class PositionState:
    """
    Trạng thái Position của SHD.

    Một Position có thể có nhiều Entry.
    """


    side: str = ""

    stage: Stage = Stage.STAGE_0


    entry_price: float = 0.0

    current_price: float = 0.0

    stop_loss: float = 0.0

    take_profit: float = 0.0


    size: float = 0.0


    is_open: bool = False


    entries: list = field(
        default_factory=list
    )



    def add_entry(
        self,
        price: float,
        size: float,
        capital: float
    ):
        """
        Thêm entry mới.
        """

        self.entries.append(

            {

                "price": price,

                "size": size,

                "capital": capital

            }

        )


        self.size += size


        self.entry_price = self.average_price()

        self.is_open = True



    def average_price(self):

        if not self.entries:

            return 0.0


        total_value = sum(

            e["price"] * e["size"]

            for e in self.entries

        )


        total_size = sum(

            e["size"]

            for e in self.entries

        )


        return total_value / total_size



    def set_risk(
        self,
        stop_loss: float,
        take_profit: float
    ):

        self.stop_loss = stop_loss

        self.take_profit = take_profit