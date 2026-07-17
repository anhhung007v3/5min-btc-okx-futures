"""
Trading Brain SHD
Stage Projection
"""


class StageProjection:
    """Build current stage from events."""

    def __init__(self):
        self.reset()

    def reset(self):
        self.stage = 0

    def apply(self, event):
        event_type = event.get("event_type") or event.get("type")

        if event_type == "STAGE_CHANGED":
            self.stage = event.get("data", {}).get("stage", 0)

    def get_stage(self):
        return self.stage