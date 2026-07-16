from brain.execution.execution_result import (
    ExecutionResult
)


class ExecutionController:
    """
    Bộ điều phối thực thi của Trading Brain SHD.

    Nhiệm vụ:

    - Nhận action đã được quyết định.
    - Gọi execution adapter.
    - Trả về ExecutionResult.


    Không:

    - Phân tích thị trường.
    - Tạo quyết định.
    - Tính Risk.
    - Quản lý Stage.
    """


    def __init__(
        self,
        executor=None
    ):

        self.executor = executor



    def execute(
        self,
        action: str,
        data: dict
    ) -> ExecutionResult:
        """
        Thực hiện action.


        V1:

        Nếu chưa có executor thật:

        chỉ mô phỏng kết quả.
        """


        if self.executor is None:

            return ExecutionResult(
                success=False,
                action=action,
                message="NO_EXECUTOR_CONNECTED",
                timestamp=self._timestamp()
            )



        try:

            result = self.executor.execute(
                action,
                data
            )


            return result



        except Exception as e:

            return ExecutionResult(
                success=False,
                action=action,
                message=str(e),
                timestamp=self._timestamp()
            )



    def _timestamp(self):

        from datetime import datetime

        return datetime.utcnow().isoformat()