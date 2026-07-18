from brain.runtime.runtime_controller import RuntimeController


def main():

    print("START FULL OPEN POSITION FLOW TEST")


    controller = RuntimeController()


    controller.startup()


    context = controller.context


    # giả lập thị trường đủ điều kiện vào lệnh

    context.trend_strength = 0.8

    context.volatility = 0.6



    # chạy cycle

    result = controller.run_cycle()


    print("MARKET:", result.market_state)

    print("DECISION:", result.decision)


    print("POSITION:", controller.position_manager.position)



    print(
        "PAPER POSITION:",
        controller.paper_trader.position
    )


    print(
        "FULL_OPEN_POSITION_FLOW_TEST_PASS"
    )



if __name__ == "__main__":

    main()