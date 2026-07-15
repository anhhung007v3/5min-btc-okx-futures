class RiskEngine:
    """
    Risk Engine của Trading Brain SHD.

    Nhiệm vụ:

    - Kiểm tra bảo vệ vị thế.
    - Xác định protection_ok.

    Không:
    - Tạo tín hiệu.
    - Mở lệnh.
    - Điều khiển Stage.
    """


    def check_protection(
        self,
        side: str,
        entry_price: float,
        current_price: float,
        stop_loss: float
    ) -> bool:
        """
        Kiểm tra vị thế đã an toàn chưa.


        LONG:

        Stop >= Entry
        => bảo vệ vốn


        SHORT:

        Stop <= Entry
        => bảo vệ vốn
        """


        if side == "LONG":

            if stop_loss >= entry_price:
                return True


        if side == "SHORT":

            if stop_loss <= entry_price:
                return True


        return False



    def calculate_profit_percent(
        self,
        side: str,
        entry_price: float,
        current_price: float
    ) -> float:
        """
        Tính % lợi nhuận hiện tại.
        """


        if side == "LONG":

            return (
                (
                    current_price
                    -
                    entry_price
                )
                /
                entry_price
            ) * 100



        if side == "SHORT":

            return (
                (
                    entry_price
                    -
                    current_price
                )
                /
                entry_price
            ) * 100


        return 0.0