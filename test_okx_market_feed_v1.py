from brain.market.okx_market_feed import (
    OKXMarketFeed
)


def main():

    print(
        "START OKX MARKET FEED V1 TEST"
    )


    feed = OKXMarketFeed()


    price = feed.get_price()


    print(
        "BTC PRICE:",
        price
    )


    assert price > 0


    print(
        "OKX_MARKET_FEED_V1_TEST_PASS"
    )


if __name__ == "__main__":

    main()