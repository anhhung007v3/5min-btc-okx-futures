from exchange.okx_client import OKXClient


def main():

    print(
        "START OKX CANDLES V1 TEST"
    )

    client = OKXClient()

    result = client.get_candles()

    candles = result["data"]

    print(
        "TOTAL CANDLES:",
        len(candles)
    )

    print(
        "LATEST CANDLE:"
    )

    print(
        candles[0]
    )

    print(
        "OKX_CANDLES_V1_TEST_PASS"
    )


if __name__ == "__main__":

    main()