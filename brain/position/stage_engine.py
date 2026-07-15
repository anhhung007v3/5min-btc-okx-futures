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
    Position Stage Engine.

    Nhiệm vụ:

    - Đánh giá điều kiện chuyển Stage.
    - Không phân tích thị trường.
    - Không quản lý vốn.
    - Không mở/đóng lệnh.
    """


    def evaluate_stage(
        self,
        current_stage: Stage,
        movement_ok: bool,
        protection_ok: bool,
        add_position_ok: bool = False
    ) -> Stage:
        """
        Đánh giá Stage tiếp theo.

        Parameters
        ----------
        current_stage:
            Stage hiện tại.

        movement_ok:
            Giá đã đi đủ xa theo hướng có lợi.

        protection_ok:
            Stop đã được bảo vệ.

        add_position_ok:
            Điều kiện cho phép tăng vị thế.
        """


        if current_stage == Stage.STAGE_0:

            if movement_ok and protection_ok:
                return Stage.STAGE_1


        if current_stage == Stage.STAGE_1:

            if add_position_ok:
                return Stage.STAGE_2


        if current_stage == Stage.STAGE_2:

            if movement_ok and protection_ok:
                return Stage.STAGE_3


        return current_stage