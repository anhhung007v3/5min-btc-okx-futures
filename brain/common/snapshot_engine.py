"""
Trading Brain SHD
Snapshot Engine

Save and load current brain state.
"""

import json
from pathlib import Path


class SnapshotEngine:
    """Manage Brain state snapshots."""

    def __init__(
        self,
        file_path="brain_snapshot.json"
    ):
        self.file_path = Path(file_path)


    def save_snapshot(
        self,
        state: dict
    ):
        """
        Save current state.
        """

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                state,
                f,
                indent=4,
                ensure_ascii=False
            )


    def load_snapshot(self):
        """
        Load saved state.
        """

        if not self.file_path.exists():

            return None


        with open(
            self.file_path,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)