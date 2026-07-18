"""
Trading Brain SHD

Runtime Controller V1A

Initialize all core components and perform startup recovery.
"""

from brain.common.brain_context import BrainContext
from brain.common.event_store import EventStore
from brain.common.snapshot_engine import SnapshotEngine
from brain.common.startup_recovery import StartupRecoveryEngine

from brain.monitor.brain_monitor import BrainMonitor

from brain.market.market_engine import MarketEngine
from brain.decision.decision_engine import DecisionEngine
from brain.risk.risk_engine import RiskEngine

from brain.execution.execution_controller import ExecutionController
from brain.execution.paper_executor import PaperExecutor

from brain.projection.projection_engine import ProjectionEngine
from brain.projection.replay_engine import ReplayEngine

from brain.brain_loop import BrainLoop

from execution.paper_trader import PaperTrader


class RuntimeController:
    """
    Runtime composition root.
    """

    def __init__(self):

        # Context
        self.context = BrainContext()

        # Memory
        self.event_store = EventStore()
        self.snapshot_engine = SnapshotEngine()

        # Monitor
        self.brain_monitor = BrainMonitor(
            event_store=self.event_store
        )

        # Engines
        self.market_engine = MarketEngine(
            monitor=self.brain_monitor
        )

        self.decision_engine = DecisionEngine(
            monitor=self.brain_monitor
        )

        self.risk_engine = RiskEngine(
            monitor=self.brain_monitor
        )

        # Execution
        self.paper_trader = PaperTrader()

        self.paper_executor = PaperExecutor(
            self.paper_trader
        )

        self.execution_controller = ExecutionController(
            executor=self.paper_executor,
            monitor=self.brain_monitor
        )

        # Projection
        self.projection_engine = ProjectionEngine()

        self.replay_engine = ReplayEngine(
            self.event_store,
            self.projection_engine
        )

        # Startup
        self.startup_recovery = StartupRecoveryEngine(
            self.snapshot_engine,
            self.replay_engine
        )

        # Brain
        self.brain_loop = BrainLoop(
            self.market_engine,
            self.decision_engine,
            self.risk_engine,
            self.execution_controller,
            self.brain_monitor
        )

    def startup(self):
        """
        Restore previous state.
        """
        return self.startup_recovery.recover()
    def run_cycle(self):
        """
        Execute one Brain cycle.
        """
        return self.brain_loop.run(self.context)

    def shutdown(self):
        """
        Shutdown runtime.
        """
        return True