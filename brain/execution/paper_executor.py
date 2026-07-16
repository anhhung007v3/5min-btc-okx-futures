from brain.execution.execution_result import (
    ExecutionResult
)


class PaperExecutor:
    """
    Adapter kết nối Trading Brain với PaperTrader.

    Nhiệm vụ:

    - Nhận action từ ExecutionController.
    - Gọi PaperTrader.
    - Chuyển kết quả sang ExecutionResult.


    Không:

    - Tạo quyết định.
    - Tính Risk.
    - Phân tích thị trường.
    """


    def __init__(
        self,
        paper_trader
    ):

        self.paper_trader = paper_trader



    def execute(
        self,
        action: str,
        data: dict
    ) -> ExecutionResult:
        """
        Thực thi action trên PaperTrader.
        """


        if action == "OPEN_POSITION":

            result = self.paper_trader.open_position(

                side=data["side"],

                entry_price=data["entry_price"],

                size=data["size"],

                stop_loss=data["stop_loss"],

                take_profit=data["take_profit"]

            )


            if result.get("status") == "OPENED":

                return ExecutionResult(
                    success=True,
                    action=action,
                    message="POSITION_OPENED",
                    timestamp=self._timestamp()
                )



            return ExecutionResult(
                success=False,
                action=action,
                message=result.get(
                    "message",
                    "OPEN_FAILED"
                ),
                timestamp=self._timestamp()
            )



        if action == "CLOSE_POSITION":

            result = self.paper_trader.close_position()


            return ExecutionResult(
                success=result,
                action=action,
                message="POSITION_CLOSED"
                if result
                else "CLOSE_FAILED",
                timestamp=self._timestamp()
            )



        return ExecutionResult(
            success=False,
            action=action,
            message="UNKNOWN_ACTION",
            timestamp=self._timestamp()
        )



    def _timestamp(self):

        from datetime import datetime

        return datetime.utcnow().isoformat()