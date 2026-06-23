
import pandas as pd
import yfinance as yf
from ticker_list import tickers


def dwn_data(tickers, start_date, end_date):
    adj_close_price = pd.DataFrame()

    for tick in tickers:
        data = yf.download(tick, start=start_date, end=end_date)

        if not data.empty:
            adj_close_price[tick] = data['Close']
        else:
            print("Data is unnavailable")
    
    return adj_close_price
