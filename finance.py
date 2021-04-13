import yfinance as yf
import pandas as pd
pd.set_option('max_columns', None)


def compare_more():
    compare_other = input("Do you want to compare other companies (Y/N)? ")
    if compare_other.lower() == 'y':
        return True
    else:
        return False


def get_ticker():
    input_tic = input("Enter a stock symbol (type 0 to compare): ")
    return input_tic


# Compares list of tickers' financial information (Will do this at least, just prints it out right now)
def compare_financials(tickers_list):
    financials_data = {}
    for ticker in tickers_list:
        yf_ticker = yf.Ticker(ticker)
        data = yf_ticker.history()
        last_quote = (data.tail(1)['Close'].iloc[0])
        # For this company, find last quote and certain financial data
        financials_data[yf_ticker.info['symbol']] = [last_quote,
                                                     yf_ticker.financials.T[['Total Revenue', 'Net Income',
                                                                            'Gross Profit', 'Research Development']]
                                                     ]
        # for r in yf_ticker.financials:
        #     total_revenue[yf_ticker].append(r.strftime("%Y") + ": " + str(yf_ticker.financials[r]['Total Revenue']/1000000000))
        #     total_revenue[yf_ticker].append(r.strftime("%Y") + ": " + str(yf_ticker.financials[r]['Net Income']/1000000000))
        #     total_revenue[yf_ticker].append(r.strftime("%Y") + ": " + str(yf_ticker.financials[r]['Gross Profit']/1000000000))
    # df = pd.DataFrame(total_revenue)
    # print(df)
    # for t in total_revenue:
    #     print(t.info['symbol'])
    #     for y in total_revenue[t]:
    #         print(y)
    for d in financials_data:
        print("\n\n" + d + ": " + str(financials_data[d][0]))
        print(financials_data[d][1].T.div(1000000000))


# Compares list of tickers' info and balance sheet information
def compare_tickers(tickers_list):
    tickers_data = {}
    # data = yf.download(' '.join(tickers_list), group_by='tickers')
    # print(data)

    # Figures for ticker.balancesheet
    total_assets, total_liab, cash, long_term_debt = [], [], [], []
    # Figures under the ticker.info
    dividend_rate, forward_eps, price_to_book, \
        earnings_quarterly_growth, peg_ratio, symbols, forward_pe = [], [], [], [], [], [], []
    for ticker in tickers_list:
        yf_ticker = yf.Ticker(ticker)
        tic_bs = yf_ticker.balancesheet
        tic_info = yf_ticker.info
        # Append all desired data from balance sheet data
        total_assets.append(tic_bs.iloc[:, 1]['Total Assets'] / 1000000000)
        total_liab.append(tic_bs.iloc[:, 1]['Total Liab'] / 1000000000)
        cash.append(tic_bs.iloc[:, 1]['Cash'] / 1000000000)
        long_term_debt.append(tic_bs.iloc[:, 1]['Long Term Debt'] / 1000000000)
        # Append all desired data from info data
        dividend_rate.append(tic_info['dividendRate'])
        forward_eps.append(tic_info['forwardEps'])
        # last_fiscal_year_end.append(tic_info['lastFiscalYearEnd'])
        price_to_book.append(tic_info['priceToBook'])
        earnings_quarterly_growth.append(tic_info['earningsQuarterlyGrowth'])
        peg_ratio.append(tic_info['pegRatio'])
        symbols.append(tic_info['symbol'])
        forward_pe.append(tic_info['forwardPE'])
    compare_dict = {
        'Symbol': symbols, 'Forward PE': forward_pe, 'Total Assets (B)': total_assets, 'Total Liabilities (B)': total_liab,
        'Cash (B)': cash, 'L/T Debt (B)': long_term_debt, 'Dividend Rate': dividend_rate, 'Forward EPS': forward_eps,
        'Price to Book': price_to_book, 'Earnings 1/4 Growth': earnings_quarterly_growth,
        'PEG Ratio': peg_ratio
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
    compare_new_tickers = True
    while compare_new_tickers:
        tic = ""
        tickers_list = []
        while tic != "0":
            new_ticker = get_ticker()
            if new_ticker == "0":
                print(' | '.join(tickers_list))
                print("calculating...")
                tic = "0"
            else:
                tickers_list.append(new_ticker)
                print("Current selected: " + " ".join(tickers_list))
        # compare_tickers(tickers_list=tickers_list)
        compare_financials(tickers_list=tickers_list)
        compare_new_tickers = compare_more()

    # for t in tickers_list:
    #     print(t)
    #     print_stock_info(t)
    return


if __name__ == '__main__':
    main()
