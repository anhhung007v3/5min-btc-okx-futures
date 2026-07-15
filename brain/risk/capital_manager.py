from dataclasses import dataclass


@dataclass
class CapitalManager:
    """
    Quản lý vốn của Trading Brain SHD.
    """

    total_capital: float

    max_usage_percent: float = 75.0

    used_capital: float = 0.0

    def max_capital(self) -> float:
        """
        Số vốn tối đa được phép sử dụng.
        """

        return self.total_capital * self.max_usage_percent / 100


    def available_capital(self) -> float:
        """
        Số vốn còn có thể sử dụng.
        """

        return self.max_capital() - self.used_capital


    def can_open(self, amount: float) -> bool:
        """
        Kiểm tra có được phép mở thêm lệnh hay không.
        """

        return amount <= self.available_capital()


    def add_position(self, amount: float):
        """
        Ghi nhận đã sử dụng thêm vốn.
        """

        self.used_capital += amount


    def close_position(self, amount: float):
        """
        Hoàn lại vốn sau khi đóng lệnh.
        """

        self.used_capital -= amount

        if self.used_capital < 0:
            self.used_capital = 0