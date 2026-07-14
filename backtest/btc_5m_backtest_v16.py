import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))


import pandas as pd

from strategy.indicators import add_indicators
from strategy.market_condition import analyze_market
from strategy.risk_manager_v3 import calculate_risk
from strategy.entry_signal_v16 import check_entry


def check_extra_filter(
    side,
    atr,
    rsi
):
    """
    Extra filter cho backtest V2
    """

    if atr <= 0:
        return False

    if side == "LONG" and rsi > 75:
        return False

    if side == "SHORT" and rsi < 25:
        return False

    return True
def check_trade_result(
    df,
    start_index,
    side,
    entry,
    stop_loss,
    take_profit
):
    """
    V4:
    - Initial SL
    - Move SL to breakeven at +1R
    - Trailing after +1.5R
    """

    risk = abs(entry - stop_loss)

    current_sl = stop_loss
    trailing_active = False

    highest = entry
    lowest = entry


    for i in range(start_index, len(df)):

        candle = df.iloc[i]

        high = candle["high"]
        low = candle["low"]


        if side == "LONG":

            # update highest price
            if high > highest:
                highest = high


            # +1R => move SL to entry
            if highest >= entry + risk:
                current_sl = entry


            # +1.5R => trailing
            if highest >= entry + (risk * 1.5):
                trailing_active = True
                current_sl = highest - risk


            if low <= current_sl:

                if current_sl == stop_loss:
                    status = "LOSS"

                elif current_sl == entry:
                    status = "BREAKEVEN"

                else:
                    status = "WIN"


                return {
                    "result": status,
                    "exit": current_sl
                }


        elif side == "SHORT":

            if low < lowest:
                lowest = low


            if lowest <= entry - risk:
                current_sl = entry


            if lowest <= entry - (risk * 1.5):
                trailing_active = True
                current_sl = lowest + risk


            if high >= current_sl:

                if current_sl == stop_loss:
                    status = "LOSS"

                elif current_sl == entry:
                    status = "BREAKEVEN"

                else:
                    status = "WIN"


                return {
                    "result": status,
                    "exit": current_sl
                }


            if low <= take_profit:
                return {
                    "result": "WIN",
                    "exit": take_profit
                }


    return {
        "result": "OPEN",
        "exit": df.iloc[-1]["close"]
    }


def run_backtest():

    print("===== BTC 5M BACKTEST V2 START =====")
    balance = 20
    max_order = 5
    leverage = 5
    fee_rate = 0.0005

    filter_stats = {
        "candles": 0,
        "signal_found": 0,
        "filter_pass": 0,

        "low_score": 0,
        "no_pullback": 0,
        "no_rejection": 0,
        "market_wait": 0,
        "score_2": 0,
        "score_4": 0,
        "score_6": 0,
        "score_8": 0,
    }

    df5 = pd.read_csv(
        "data/btc_5m.csv"
    )


    df5 = df5.sort_values(
        "ts"
    )


    df5["open"] = df5["open"].astype(float)
    df5["high"] = df5["high"].astype(float)
    df5["low"] = df5["low"].astype(float)
    df5["close"] = df5["close"].astype(float)
    df5["volume"] = df5["volume"].astype(float)


    df5 = add_indicators(
        df5
    )


    total_trade = 0
    win = 0
    loss = 0
    open_trade = 0
    breakeven = 0
    balance = 20
    max_order = 5
    # performance metrics
    total_profit = 0
    total_loss = 0

    peak_balance = balance
    max_drawdown = 0

    # signal statistics
    signal_found = 0
    filter_pass = 0

    trades = []



    for i in range(50, len(df5)-20):

        filter_stats["candles"] += 1


        history = df5.iloc[:i]


        market = analyze_market(
            history
        )


        signal = check_entry(
            market,
            history
        )

        score = int(signal["score"].split("/")[0])

        if score == 2:
            filter_stats["score_2"] += 1
        elif score == 4:
            filter_stats["score_4"] += 1
        elif score == 6:
            filter_stats["score_6"] += 1
        elif score == 8:
            filter_stats["score_8"] += 1

        if signal["signal"] != "NO_ENTRY":
            signal_found += 1
            filter_stats["signal_found"] += 1
        if signal["reason"] == "LOW_SCORE":
            filter_stats["low_score"] += 1

        elif signal["reason"] == "NO_PULLBACK":
            filter_stats["no_pullback"] += 1

        elif signal["reason"] == "NO_REJECTION":
            filter_stats["no_rejection"] += 1

        elif signal["reason"] == "MARKET_WAIT":
            filter_stats["market_wait"] += 1


        if signal["signal"] not in [
            "LONG_READY",
            "SHORT_READY"
        ]:
            continue



        side = (
            "LONG"
            if signal["signal"] == "LONG_READY"
            else "SHORT"
        )


        entry = signal["price"]


        atr = history.iloc[-2]["atr"]


        risk = calculate_risk(
            side,
            entry,
            atr
        )
        if not check_extra_filter(
            side,
            atr,
            history.iloc[-2]["rsi"]
        ):
            continue

        filter_pass += 1
        filter_stats["filter_pass"] += 1


        result = check_trade_result(
            df5,
            i,
            side,
            entry,
            risk["stop_loss"],
            risk["take_profit"]
        )
        position_value = max_order * leverage
        fee = position_value * fee_rate * 2

        if side == "LONG":
            pnl = position_value * (
                result["exit"] - entry
            ) / entry

        else:
            pnl = position_value * (
                entry - result["exit"]
            ) / entry


        pnl_after_fee = pnl - fee

        balance += pnl_after_fee
        if pnl_after_fee > 0:
            total_profit += pnl_after_fee

        elif pnl_after_fee < 0:
            total_loss += abs(pnl_after_fee)


        if balance > peak_balance:
            peak_balance = balance


        drawdown = peak_balance - balance

        if drawdown > max_drawdown:
            max_drawdown = drawdown

        trades.append(
            {
                "side": side,
                "entry": entry,
                "exit": result["exit"],
                "stop_loss": risk["stop_loss"],
                "take_profit": risk["take_profit"],
                "size_usdt": max_order,
                "position_value": position_value,
                "pnl": pnl,
                "fee": fee,
                "pnl_after_fee": pnl_after_fee,
                "balance": balance,
                "result": result["result"]
            }
        )

        trade = {
            "result": result,
            "side": side,
            "entry": entry,
            "atr": atr,

            "trend": market["trend"],
            "decision": market["decision"],

            "volume_ratio": history.iloc[-2]["volume_ratio"],
            "rsi": history.iloc[-2]["rsi"],

            "ema20": history.iloc[-2]["ema20"],
            "ema50": history.iloc[-2]["ema50"],

            "distance": abs(
                history.iloc[-2]["close"]
                -
                history.iloc[-2]["ema20"]
            ) / history.iloc[-2]["ema20"],

            "pullback": signal["details"]["pullback"],
            "rejection": signal["details"]["rejection"]
        }


        print(
            "TRADE DATA:",
            trade
        )


        if result == "LOSS":
            print(
                "LOSS:",
                side,
                "Entry:",
                entry,
                "SL:",
                risk["stop_loss"],
                "TP:",
                risk["take_profit"]
            )


        total_trade += 1


        print(
            "TRADE",
            signal["signal"],
            "SCORE:",
            signal["score"],
            "PULLBACK:",
            signal["details"]["pullback"],
            "REJECTION:",
            signal["details"]["rejection"],
            "VOLUME:",
            signal["details"]["volume"],
            "ENTRY:",
            signal["price"],
            "SL:",
            risk["stop_loss"],
            "TP:",
            risk["take_profit"],
            "ATR:",
            risk["atr"],
            "RESULT:",
            result
        )

        if signal["details"]["pullback"] == "YES":
            print(">>> PULLBACK:", result)
        else:
            print(">>> NO PULLBACK:", result)

        if result["result"] == "WIN":
            win += 1

        elif result["result"] == "LOSS":
            loss += 1

        elif result["result"] == "BREAKEVEN":
            breakeven += 1

        else:
            open_trade += 1



    print()
    print("\n===== TRADE DETAILS =====")

    for idx, trade in enumerate(trades, 1):
        print(
            idx,
            trade
        )
    print("===== RESULT =====")

    print(
        "TOTAL TRADES:",
        total_trade
    )

    print(
        "WIN:",
        win
    )

    print(
        "LOSS:",
        loss
    )

    print(
        "OPEN:",
        open_trade
    )


    if total_trade > 0:

        win_rate = (
            win / total_trade
        ) * 100

        print(
            "WIN RATE:",
            round(win_rate,2),
            "%"
        )
    print()

    print(
        "FINAL BALANCE:",
        round(balance,6)
    )


    print(
        "TOTAL PNL:",
        round(balance - 20,6)
    )


    print(
        "ROI:",
        round(((balance - 20) / 20) * 100,3),
        "%"
    )


    if total_loss > 0:

        profit_factor = (
            total_profit / total_loss
        )

        print(
            "PROFIT FACTOR:",
            round(profit_factor,3)
        )


    if win > 0:

        print(
            "AVERAGE WIN:",
            round(total_profit / win,6)
        )


    if loss > 0:

        print(
            "AVERAGE LOSS:",
            round(total_loss / loss,6)
        )


    print(
        "MAX DRAWDOWN:",
        round(max_drawdown,6)
    )
    print(
        "BREAKEVEN:",
        breakeven
    )
    print()

    print(
        "SIGNAL FOUND:",
        signal_found
    )

    print(
        "FILTER PASS:",
        filter_pass
    )
    print(
        "LOW SCORE:",
        filter_stats["low_score"]
    )

    print(
        "NO PULLBACK:",
        filter_stats["no_pullback"]
    )

    print(
        "NO REJECTION:",
        filter_stats["no_rejection"]
    )

    print(
        "MARKET WAIT:",
        filter_stats["market_wait"]
    )

    print()

    print("===== FILTER STATISTICS =====")

    print(
        "SCORE 2:",
        filter_stats["score_2"]
    )

    print(
        "SCORE 4:",
        filter_stats["score_4"]
    )

    print(
        "SCORE 6:",
        filter_stats["score_6"]
    )

    print(
        "SCORE 8:",
        filter_stats["score_8"]
    )

    print(
        "TOTAL CANDLES:",
        filter_stats["candles"]
    )

    print(
        "SIGNAL FOUND:",
        filter_stats["signal_found"]
    )

    print(
        "FILTER PASS:",
        filter_stats["filter_pass"]
    )



if __name__ == "__main__":

    run_backtest()