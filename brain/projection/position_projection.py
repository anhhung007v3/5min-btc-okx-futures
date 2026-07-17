"""
Trading Brain SHD
Position Projection
"""


class PositionProjection:
    """Build current position from events."""

    def __init__(self):
        self.reset()

    def reset(self):
        self.position = None

    def apply(self, event):
        event_type = event.get("event_type") or event.get("type")

        if event_type == "POSITION_OPENED":
            self.position = event.get("data", {}).copy()

        elif event_type == "POSITION_CLOSED":
            self.position = None

    def get_position(self):
        return self.position