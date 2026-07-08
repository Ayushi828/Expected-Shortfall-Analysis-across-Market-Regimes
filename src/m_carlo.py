import numpy as np

def cal_var_mcs(returns, wt , value, c, d, s):
    
    mean_returns = returns.mean()          
    cov_mat = returns.cov() * 248       
        
    portf_mean = np.dot(wt, mean_returns) * 248
    std_dev = np.sqrt(wt.T @ cov_mat @ wt)
        
    x_mean = portf_mean * (d / 248)
    x_stdev  = std_dev  * np.sqrt(d / 248)
        
    sim_returns = np.random.normal(x_mean, x_stdev, s)
    simulated_pnl = value * sim_returns    
    
    VAR_MS = -np.percentile(simulated_pnl, 100 * (1 - c))
    
    return VAR_MS, simulated_pnl                                
