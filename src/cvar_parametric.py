import numpy as np
from scipy.stats import norm 


def cal_cvar_p(cl, value, retu_rn, wt, d):
    z = norm.ppf(cl)
    cov_mat = retu_rn.cov() * 248
    std_dev = np.sqrt(wt.T @ cov_mat @ wt)
    CVAR = []

    cvar = value * std_dev * (norm.pdf(z)/(1-cl)) * np.sqrt(d/248)
    CVAR.append(cvar)

    return CVAR
