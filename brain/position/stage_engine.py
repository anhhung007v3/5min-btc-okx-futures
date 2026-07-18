from enum import Enum



class Stage(Enum):
    """
    Giai đoạn của Position trong Trading Brain SHD.
    """

    NONE = -1

    STAGE_0 = 0

    STAGE_1 = 1

    STAGE_2 = 2

    STAGE_3 = 3

    END = 99





class StageEngine:
    """
    Position Stage Engine V2.

    Nhiệm vụ:

    - Đánh giá tiến trình Position.
    - Dùng movement + protection + profit.
    - Không:
        + Phân tích thị trường.
        + Quản lý vốn.
        + Mở/đóng lệnh.
    """



    def evaluate_stage(

        self,

        current_stage: Stage,

        movement_ok: bool,

        protection_ok: bool,

        profit_percent: float = 0.0,

        add_position_ok: bool = False

    ) -> Stage:


        if current_stage == Stage.STAGE_0:


            if movement_ok and protection_ok:

                return Stage.STAGE_1



        if current_stage == Stage.STAGE_1:


            if profit_percent >= 2.0:

                return Stage.STAGE_2



        if current_stage == Stage.STAGE_2:


            if (

                profit_percent >= 5.0

                and

                protection_ok

            ):

                return Stage.STAGE_3



        return current_stage