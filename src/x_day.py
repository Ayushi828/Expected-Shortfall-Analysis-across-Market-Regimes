
def xday_return_calc(historical_returns, d):
  xdays_return = historical_returns.rolling(window = d).sum()
  xdays_return = xdays_return.dropna()
  return xdays_return
  
