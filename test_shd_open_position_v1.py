from brain.runtime.runtime_controller import RuntimeController


def main():

    runtime = RuntimeController()


    context = runtime.context


    context.market_price = 64000


    context.candles = []


    context.indicators = {

        "ema20": 64100,

        "ema50": 64000,

        "rsi": 60,

        "atr": 20,

        "volume_ratio": 1.2

    }


    context.market_state = type(

        "MarketState",

        (),

        {

            "movement_ok": True,

            "trend_strength": 0.8,

            "volatility": 0.01

        }

    )()



    context.position = None



    result = runtime.entry_signal_engine.evaluate(

        context.market_state,

        context.indicators

    )


    print(
        "ENTRY SIGNAL:",
        result
    )



    decision = runtime.decision_engine.evaluate(

        position=None,

        market_state=context.market_state,

        entry_signal=result,

        exit_signal=None

    )


    print(

        "DECISION:",

        decision

    )



    if decision["decision"] == "OPEN":


        plan = runtime.trade_planner.create_plan(

            signal=result,

            price=context.market_price

        )


        print(

            "PLAN:",

            plan

        )



        opened = runtime.position_manager.open_position(

            side=plan["side"],

            price=plan["price"],

            size=plan["size"],

            capital=plan["capital"],

            stop_loss=plan["stop_loss"],

            take_profit=plan["take_profit"]

        )


        print(

            "POSITION OPEN:",
            opened

        )


        print(

            "POSITION:",
            runtime.position_manager.position

        )



if __name__ == "__main__":

    main()