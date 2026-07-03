import numpy as np

def hist_return(returns, w):
    h_return =  (returns * w).sum(axis = 1)
    h_return = h_return.dropna
    print("HISTORICAL RETURNS OF PORTFOLIO")
    print(h_return)

    return h_return
