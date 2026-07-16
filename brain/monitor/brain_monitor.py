from pathlib import Path
from typing import List

from brain.monitor.monitor_event import (
    MonitorEvent
)



class BrainMonitor:
    """
    Monitor Layer của Trading Brain SHD.

    Nhiệm vụ:

    - Nhận event từ các module.
    - Lưu lịch sử hoạt động.
    - Xuất log quan sát.


    Không:

    - Ra quyết định.
    - Điều khiển Position.
    - Gửi lệnh.
    """


    def __init__(
        self,
        log_file: str = "brain_monitor.log"
    ):

        self.events: List[MonitorEvent] = []

        self.log_file = Path(
            log_file
        )



    def record(
        self,
        event: MonitorEvent
    ):
        """
        Ghi nhận một sự kiện Brain.
        """


        self.events.append(
            event
        )


        self._write_log(
            event
        )



    def get_events(
        self
    ) -> List[MonitorEvent]:
        """
        Lấy toàn bộ lịch sử event.
        """

        return self.events



    def _write_log(
        self,
        event: MonitorEvent
    ):
        """
        Ghi event ra file log.
        """


        with open(
            self.log_file,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(
                f"{event.timestamp} | "
                f"{event.event_type} | "
                f"{event.message}\n"
            )