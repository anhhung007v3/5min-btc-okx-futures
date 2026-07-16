from brain.execution.execution_result import (
    ExecutionResult
)

from brain.monitor.monitor_event import (
    MonitorEvent
)


class ExecutionController:
    """
    Điều khiển tầng thực thi SHD.
    """

    def __init__(
        self,
        executor,
        monitor=None
    ):

        self.executor = executor

        self.monitor = monitor



    def open_position(
        self,
        side: str,
        price: float,
        size: float,
        stop_loss: float,
        take_profit: float
    ) -> ExecutionResult:

        data = {

            "side": side,

            "entry_price": price,

            "size": size,

            "stop_loss": stop_loss,

            "take_profit": take_profit

        }


        result = self.executor.execute(

            action="OPEN_POSITION",

            data=data

        )


        if self.monitor:

            self.monitor.record(

                MonitorEvent(

                    event_type="EXECUTION_RESULT",

                    message=result.message,

                    timestamp=result.timestamp,

                    data={

                        "success": result.success,

                        "action": result.action

                    }

                )

            )


        return result