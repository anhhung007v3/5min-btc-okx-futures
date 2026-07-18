from exchange.okx_client import (
    OKXClient
)


class OKXMarketFeed:
    """
    Convert OKX market data
    into SHD usable format.
    """


    def __init__(
        self
    ):

        self.client = OKXClient()



    def get_price(
        self
    ) -> float:
        """
        Return BTC current price.
        """


        data = (
            self.client
            .get_btc_price()
        )


        price = float(

            data["data"][0]["last"]

        )


        return price