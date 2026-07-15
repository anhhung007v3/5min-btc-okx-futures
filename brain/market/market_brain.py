from brain.common.models import MarketContext


class MarketBrain:
    """
    Market Brain

    Nhiệm vụ:
    - Quan sát thị trường.
    - Phân tích trạng thái thị trường.
    - Trả về MarketContext.

    Không được:
    - Mở lệnh.
    - Đóng lệnh.
    - Quản lý vốn.
    """

    def analyze(self, market_data) -> MarketContext:
        """
        Phân tích dữ liệu thị trường.

        Parameters
        ----------
        market_data
            Dữ liệu OHLCV.

        Returns
        -------
        MarketContext
        """

        raise NotImplementedError(
            "MarketBrain.analyze() chưa được triển khai."
        )