import numpy as np

def cal_var_ms(returns, w, value, c, d, s):
    Var_ms = []

    cov_mat = returns.cov() * 250
    mean_returns = returns.mean()
    c_matrix = returns.cov() * 250

    value_mean = np.dot(w, returns)* 250
    std_dev = np.sqrt(w.T @ cov_mat @ w)

    nday_mean = value * (d/ 250)
    nday_std = std_dev * np.sqrt(d/250)

    sim_returns = np.random.normal(nday_mean, nday_std, s)

    sim_pnl = value * sim_returns

    var_s = -np.percentile(sim_pnl, 100*(1-c))
    Var_ms.append(var_s)
    print("VaR calculated through monte carlo is", Var_ms)
    return Var_ms, sim_pnl
