"""
Trading Brain SHD

Runtime Controller V1B

Initialize all core components and perform startup recovery.
"""


from brain.common.brain_context import (
    BrainContext
)

from brain.common.event_store import (
    EventStore
)

from brain.common.snapshot_engine import (
    SnapshotEngine
)

from brain.common.startup_recovery import (
    StartupRecoveryEngine
)

from brain.common.position_snapshot import (
    PositionSnapshot
)


from brain.monitor.brain_monitor import (
    BrainMonitor
)


from brain.market.market_engine import (
    MarketEngine
)

from brain.decision.decision_engine import (
    DecisionEngine
)

from brain.decision.entry_signal_engine import (
    EntrySignalEngine
)

from brain.decision.trade_planner import (
    TradePlanner
)


from brain.position.position_manager import (
    PositionManager
)

from brain.risk.capital_manager import (
    CapitalManager
)

from brain.risk.risk_engine import (
    RiskEngine
)

from brain.risk.exit_signal_engine import (
    ExitSignalEngine
)


from brain.execution.execution_controller import (
    ExecutionController
)

from brain.execution.paper_executor import (
    PaperExecutor
)


from brain.projection.projection_engine import (
    ProjectionEngine
)

from brain.projection.replay_engine import (
    ReplayEngine
)


from brain.brain_loop import (
    BrainLoop
)


from execution.paper_trader import (
    PaperTrader
)



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


        self.entry_signal_engine = EntrySignalEngine(

            monitor=self.brain_monitor

        )



        self.trade_planner = TradePlanner()



        self.capital_manager = CapitalManager(

            total_capital=20

        )



        self.position_manager = PositionManager(

            self.capital_manager,
            self.snapshot_engine

        )



        self.risk_engine = RiskEngine(

            monitor=self.brain_monitor

        )


        self.exit_signal_engine = ExitSignalEngine()



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

            self.entry_signal_engine,

            self.exit_signal_engine,

            self.decision_engine,

            self.trade_planner,

            self.position_manager,

            self.risk_engine,

            self.execution_controller,

            self.brain_monitor

        )



    def startup(self):
        """
        Restore previous state.
        """


        snapshot = (

            self.startup_recovery

            .recover()

        )


        if snapshot:


            position = PositionSnapshot.from_dict(

                snapshot

            )


            self.position_manager.position = position


            self.context.position = position



        return snapshot



    def run_cycle(self):
        """
        Execute one Brain cycle.
        """

        return self.brain_loop.run(

            self.context

        )



    def shutdown(self):
        """
        Shutdown runtime.
        """

        return True