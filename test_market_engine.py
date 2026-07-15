from brain.market.market_engine import (
    MarketEngine
)


def main():

    print("===== SHD MARKET ENGINE TEST =====")


    engine = MarketEngine()



    print("\n1. STRONG MARKET")


    state = engine.evaluate(
        trend_strength=0.8,
        volatility=0.6
    )


    print("DIRECTION:")
    print(state.direction)


    print("TREND STRENGTH:")
    print(state.trend_strength)


    print("VOLATILITY:")
    print(state.volatility)


    print("MOVEMENT OK:")
    print(state.movement_ok)



    print("\n2. WEAK MARKET")


    state = engine.evaluate(
        trend_strength=0.3,
        volatility=0.2
    )


    print("DIRECTION:")
    print(state.direction)


    print("TREND STRENGTH:")
    print(state.trend_strength)


    print("VOLATILITY:")
    print(state.volatility)


    print("MOVEMENT OK:")
    print(state.movement_ok)



if __name__ == "__main__":
    main()