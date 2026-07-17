"""
Trading Brain SHD
Projection Engine

Read events from EventStore and build current state.
"""

from brain.projection.position_projection import PositionProjection
from brain.projection.stage_projection import StageProjection


class ProjectionEngine:
    """Base projection engine."""

    def __init__(self):
        self.projections = {
            "position": PositionProjection(),
            "stage": StageProjection(),
        }

    def register(self, name, projection):
        self.projections[name] = projection

    def apply(self, event):
        for projection in self.projections.values():
            projection.apply(event)

    def reset(self):
        for projection in self.projections.values():
            projection.reset()

    def get_projection(self, name):
        """Return a projection by name."""
        return self.projections.get(name)

    def replay(self, events):
        """Replay a list of events."""
        self.reset()

        for event in events:
            self.apply(event)