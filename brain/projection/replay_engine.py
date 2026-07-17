"""
Trading Brain SHD
Replay Engine

Replay events from EventStore into ProjectionEngine.
"""


class ReplayEngine:
    """Replay events into ProjectionEngine."""

    def __init__(self, event_store, projection_engine):
        self.event_store = event_store
        self.projection_engine = projection_engine

    def rebuild(self):
        """Rebuild projections from all stored events."""
        events = self.event_store.load_events()
        self.projection_engine.replay(events)