
import pandas as pd
import numpy as np
import datetime as dt
import scipy.stats as norm


from dataa.h_data import (get_price)
from dataa.ticker_list import (tickers)
from dataa.wt_distribution import (wt_distribution)
from src.returns import (cal_returns)
from src.hist_return import hist_return
from src.var_parametric import cal_var_s
from src.cvar_para import cal_cvar_p

years = 25
portfolio = float(input("Enter portfolio value in Rs : "))
confidence = float(input("Enter the confidence for both VaR and CVaR calculation: "))
days = int(input("Enter the time window for calculation: "))


