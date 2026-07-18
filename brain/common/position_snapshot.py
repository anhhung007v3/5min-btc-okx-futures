"""
Trading Brain SHD

Position Snapshot Converter V1

Convert PositionState <-> dict
for SnapshotEngine persistence.
"""

from brain.position.position_state import (
    PositionState
)

from brain.position.stage_engine import (
    Stage
)



class PositionSnapshot:
    """
    Convert PositionState
    to snapshot data and restore back.

    Không:
    - lưu file
    - quản lý snapshot
    - điều khiển position
    """



    @staticmethod
    def to_dict(
        position
    ):
        """
        Convert PositionState to dict.
        """

        if position is None:

            return None


        return {

            "side": position.side,

            "stage": position.stage.name,

            "entry_price": position.entry_price,

            "current_price": position.current_price,

            "stop_loss": position.stop_loss,

            "take_profit": position.take_profit,

            "size": position.size,

            "is_open": position.is_open,

            "entries": position.entries

        }



    @staticmethod
    def from_dict(
        data
    ):
        """
        Restore PositionState from dict.
        """

        if data is None:

            return None



        position = PositionState(

            side=data.get(
                "side",
                ""
            ),

            stage=Stage[
                data.get(
                    "stage",
                    "STAGE_0"
                )
            ]

        )



        position.entry_price = data.get(
            "entry_price",
            0.0
        )


        position.current_price = data.get(
            "current_price",
            0.0
        )


        position.stop_loss = data.get(
            "stop_loss",
            0.0
        )


        position.take_profit = data.get(
            "take_profit",
            0.0
        )


        position.size = data.get(
            "size",
            0.0
        )


        position.is_open = data.get(
            "is_open",
            False
        )


        position.entries = data.get(
            "entries",
            []
        )


        return position