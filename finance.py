import yfinance as yf
import pandas as pd


def get_ticker():
    input_tic = input("Enter a stock symbol (type 0 to quit): ")
    return input_tic


def compare_tickers(tickers_list):
    tickers_data = {}
    # data = yf.download(' '.join(tickers_list), group_by='tickers')
    # print(data)
    symbols = []
    forwardPE = []
    for ticker in tickers_list:
        tf_ticker = yf.Ticker(ticker)
        print(tf_ticker.balancesheet)
        symbols.append(tf_ticker.info['symbol'])
        forwardPE.append(tf_ticker.info['forwardPE'])
    compare_dict = {
        'Symbol': symbols,
        'Forward PE': forwardPE
    }
    print(pd.DataFrame(compare_dict))
    #     ticker_object = yf.Ticker(ticker)
    #
    #     # convert info() output from dictionary to dataframe
    #     temp = pd.DataFrame.from_dict(ticker_object.info, orient="index")
    #     temp.reset_index(inplace=True)
    #     # temp.columns = ["Attribute", "Recent"]
    #     temp.columns = tickers_list
    #     tickers_data[ticker] = temp
    # combined_data = pd.concat(tickers_data)
    # combined_data = combined_data.reset_index()
    # del combined_data["level_1"]  # clean up unnecessary column
    # combined_data.columns = ["Ticker", "Attribute", "Recent"]  # update column names

    # print(combined_data)


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
            print("calculating...")
            tic = "0"
        else:
            tickers_list.append(new_ticker)
            print(tickers_list)
    print(tickers_list)
    compare_tickers(tickers_list=tickers_list)
    # for t in tickers_list:
    #     print(t)
    #     print_stock_info(t)
    return


if __name__ == '__main__':
    main()
