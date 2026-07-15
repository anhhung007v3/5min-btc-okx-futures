from strategy.position_size import calculate_position_size


print("===== POSITION SIZE LIVE LEVERAGE TEST =====")


result = calculate_position_size(

    balance=20,

    risk_percent=1,

    entry_price=62500,

    stop_loss=62100,

    leverage=3

)


print(result)