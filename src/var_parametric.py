import numpy as np
from scipy.stats import norm


def covar_stddev(returns, w):
    cov_mat = returns.cov() * 248
    std_dev = np.sqrt(w.T @ cov_mat @ w)

    return cov_mat, std_dev

def cal_var_p(value, std_dev, cl, d):
    VAR_p= []
    var_p =  value * std_dev * norm.ppf(cl) *np.sqrt(d/248)
    VAR_p.append(var_p)
    
    return VAR_p



