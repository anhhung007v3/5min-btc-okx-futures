from datetime import datetime


from brain.common.brain_context import (
    BrainContext
)


from brain.monitor.monitor_event import (
    MonitorEvent
)


class BrainLoop:

    def __init__(

        self,

        market_engine,

        indicator_engine,

        entry_signal_engine,

        exit_signal_engine,

        decision_engine,

        trade_planner,

        position_manager,

        risk_engine,

        execution_controller,

        brain_monitor

    ):

        self.market_engine = market_engine

        self.indicator_engine = indicator_engine

        self.entry_signal_engine = entry_signal_engine

        self.exit_signal_engine = exit_signal_engine

        self.decision_engine = decision_engine

        self.trade_planner = trade_planner

        self.position_manager = position_manager

        self.risk_engine = risk_engine

        self.execution_controller = execution_controller

        self.brain_monitor = brain_monitor

        self.okx_market_feed = None



    def run(

        self,

        context: BrainContext

    ):

        # OKX MARKET PRICE

        print(
            "BTC PRICE:",
            context.market_price
        )

        print(
            "CANDLES:",
            len(context.candles)
            if context.candles
            else 0
        )

        if self.okx_market_feed:

            context.market_price = (
                self.okx_market_feed.get_price()
            )



        # INDICATORS

        context.indicators = (

            self.indicator_engine.calculate(

                context.candles

            )

        )

        if context.indicators:

            ema20 = context.indicators["ema20"]

            ema50 = context.indicators["ema50"]

            atr = context.indicators["atr"]


            context.trend_strength = abs(
                ema20 - ema50
            ) / ema50


            context.volatility = (
                atr /
                context.market_price
            )

        # MARKET

        context.market_state = (

            self.market_engine.evaluate(

                trend_strength=context.trend_strength,

                volatility=context.volatility

            )

        )

        print(

            "INDICATORS:",

            context.indicators

        )



        # ENTRY SIGNAL

        context.entry_signal = (

            self.entry_signal_engine.evaluate(

                context.market_state,

                context.indicators

            )

        )

        print(
            "MARKET STATE:",
            context.market_state.__dict__
        )



        # EXIT SIGNAL

        if context.position is not None:

            context.exit_signal = (

                self.exit_signal_engine.evaluate(

                    context.position,

                    context.position.current_price

                )

            )

        else:

            context.exit_signal = None



        # DECISION

        context.decision = (

            self.decision_engine.evaluate(

                position=context.position,

                market_state=context.market_state,

                entry_signal=context.entry_signal,

                exit_signal=context.exit_signal

            )

        )



        # RISK

        if context.position is not None:

            context.protection_ok = (

                self.risk_engine.check_protection(

                    context.position

                )

            )


            context.profit_percent = (

                self.risk_engine.calculate_profit_percent(

                    side=context.position.side,

                    entry_price=context.position.entry_price,

                    current_price=context.position.current_price

                )

            )


        # TRADE PLANNING

        if (

            context.decision["decision"] == "OPEN"

        ):

            plan = self.trade_planner.create_plan(

                signal=context.entry_signal,

                price=context.market_price

            )

            if plan:


                self.position_manager.open_position(

                    side=plan["side"],

                    price=plan["price"],

                    size=plan["size"],

                    capital=plan["capital"],

                    stop_loss=plan["stop_loss"],

                    take_profit=plan["take_profit"]

                )


                context.position = (

                    self.position_manager.position

                )



        # EXECUTION OPEN

        if (

            context.decision["decision"] == "OPEN"

            and

            context.position is not None

        ):


            context.execution_result = (

                self.execution_controller.open_position(

                    side=context.position.side,

                    price=context.position.entry_price,

                    size=context.position.size,

                    stop_loss=context.position.stop_loss,

                    take_profit=context.position.take_profit

                )

            )



        # EXECUTION CLOSE

        if (

            context.decision["decision"] == "CLOSE"

        ):


            context.execution_result = (

                self.execution_controller.close_position()

            )


            self.position_manager.close_position()

            context.position = None



        # MONITOR

        if self.brain_monitor:

            self.brain_monitor.record(

                MonitorEvent(

                    event_type="BRAIN_CYCLE_COMPLETE",

                    message="CYCLE_FINISHED",

                    timestamp=datetime.utcnow().isoformat(),

                    data={

                        "decision": context.decision,

                        "protection_ok": context.protection_ok

                    }

                )

            )



        return context