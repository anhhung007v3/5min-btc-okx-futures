import json

from pathlib import Path
from typing import List

from brain.monitor.monitor_event import (
    MonitorEvent
)


class EventStore:
    """
    Lưu lịch sử event lâu dài cho SHD.

    Nhiệm vụ:

    - Lưu MonitorEvent.
    - Đọc lại lịch sử.

    Không:

    - Ra quyết định.
    - Phân tích.
    - Điều khiển hệ thống.
    """


    def __init__(
        self,
        file_path: str = "brain_history.json"
    ):

        self.file_path = Path(
            file_path
        )


    def save_event(
        self,
        event: MonitorEvent
    ):

        events = self.load_events()


        events.append(
            {
                "event_type": event.event_type,

                "message": event.message,

                "timestamp": event.timestamp,

                "data": event.data
            }
        )


        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                events,
                f,
                indent=4,
                ensure_ascii=False
            )



    def load_events(
        self
    ) -> List[dict]:

        if not self.file_path.exists():

            return []


        with open(
            self.file_path,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)