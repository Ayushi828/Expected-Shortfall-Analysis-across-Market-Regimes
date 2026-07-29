import numpy as np
weigh = []

def wt_distribution(tickers):
    print("\n",'-'*10, "\tFor weight of portfolio", '-'*10)

    print("\n a) Equally distributed \n b) Insert weight of each stock \n")
    ch = str(input("choose the option for weight distribution: "))

    if ch == 'a':
        weight = np.array([1/len(tickers)] * len(tickers))

    else: 
        for w in range(1,11):
            w = float(input(f"weight for stock{w} : \t" ))
            weigh.append(w)

    return weigh
