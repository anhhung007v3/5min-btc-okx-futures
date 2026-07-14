class TraderInterface:


    def get_position(self):

        raise NotImplementedError


    def open_position(
        self,
        side,
        entry_price,
        size,
        stop_loss,
        take_profit
    ):

        raise NotImplementedError


    def close_position(self):

        raise NotImplementedError


    def check_exit(
        self,
        current_price
    ):

        raise NotImplementedError