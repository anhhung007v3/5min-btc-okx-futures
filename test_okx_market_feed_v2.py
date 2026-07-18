from exchange.okx_market_feed import (
    OKXMarketFeed
)


def main():

    print(
        "START OKX MARKET FEED V2 TEST"
    )


    feed = OKXMarketFeed()


    price = (
        feed.get_price()
    )


    print(
        "BTC PRICE:",
        price
    )


    print(
        "OKX_MARKET_FEED_V2_TEST_PASS"
    )



if __name__ == "__main__":

    main()