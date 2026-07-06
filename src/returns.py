import numpy as np

def cal_returns(adj_close_price):
    returns = np.log(adj_close_price/adj_close_price.shift(1))
    returns = returns.dropna()
    print("RETURNS")
    print(returns)

    return returns