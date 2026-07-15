from brain.position.stage_engine import (
    Stage
)


class DecisionEngine:
    """
    Decision Brain SHD V1.

    Nhiệm vụ:

    - Kết hợp Market + Position.
    - Đưa ra quyết định cấp cao.

    Không:
    - Gửi lệnh.
    - Quản lý vốn.
    - Tính Risk.
    """


    def evaluate(
        self,
        position,
        market_state
    ):

        if position is None:

            return {
                "decision": "WAIT",
                "reason": "NO_POSITION"
            }



        if market_state.movement_ok:

            if position.stage == Stage.STAGE_0:

                return {
                    "decision": "HOLD",
                    "reason": "WAIT_PROTECTION"
                }



            if position.stage == Stage.STAGE_1:

                return {
                    "decision": "DEVELOP",
                    "reason": "POSITION_SAFE"
                }



            if position.stage == Stage.STAGE_2:

                return {
                    "decision": "MANAGE",
                    "reason": "PROFIT_PROTECTION"
                }



        return {
            "decision": "HOLD",
            "reason": "MARKET_NOT_READY"
        }