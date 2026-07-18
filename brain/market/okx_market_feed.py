"""
Trading Brain SHD

OKX Market Feed V1

Read market data from OKX.
"""


from exchange.okx_client import (
    OKXClient
)



class OKXMarketFeed:
    """
    Adapter giữa OKX và SHD Market Engine.

    Nhiệm vụ:

    - Lấy giá BTC hiện tại.
    - Chuẩn hóa dữ liệu.

    Không:

    - Ra quyết định.
    - Mở lệnh.
    - Quản lý Position.
    """


    def __init__(
        self
    ):

        self.client = OKXClient()



    def get_price(
        self
    ) -> float:
        """
        Lấy giá BTC hiện tại.
        """


        response = (
            self.client
            .get_btc_price()
        )


        ticker = response["data"][0]


        price = float(
            ticker["last"]
        )


        return price