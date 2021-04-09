import yfinance as yf


def get_ticker():
    tic = input("Enter a stock symbol (type 0 to quit): ")
    return tic


def print_stock_info(ticker):
    # print(ticker.actions)
    # print(ticker.balancesheet)
    print(ticker.cashflow)


def main():
    tic = ""
    while tic != "0":
        tic = get_ticker()
        print_stock_info(yf.Ticker(tic))
    return


if __name__ == '__main__':
    main()
