import yfinance as yf


def get_ticker():
    input_tic = input("Enter a stock symbol (type 0 to quit): ")
    return input_tic


def print_stock_info(ticker):
    # print(ticker.actions)
    # print(ticker.balancesheet)
    print(yf.Ticker(ticker).cashflow)


def main():
    tic = ""
    tickers_list = []
    while tic != "0":
        new_ticker = get_ticker()
        if new_ticker == "0":
            print("DIDN'T GET THAT")
            tic = "0"
        else:
            tickers_list.append(new_ticker)
            print(tickers_list)
    print(tickers_list)
    for t in tickers_list:
        print(t)
        print_stock_info(t)
    return


if __name__ == '__main__':
    main()
