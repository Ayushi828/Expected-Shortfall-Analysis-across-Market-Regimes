import numpy as np


def wt_distribution(tickers):
    print("\n",'-'*10, "\tFor weight of portfolio", '-'*10)
    print("\n a) Equally distributed \n b) Insert weight of each stock \n")
    ch = str(input("choose the option for weight distribution: "))
    weigh = []

    if ch == 'a'or ch == 'A':
        weigh = np.array([1/len(tickers)] * len(tickers))

    elif ch == 'b' or ch == 'B':
        for w in range(len(tickers)):
            w = float(input(f"weight for stock{w+1} : \t" ))
            weigh.append(w)
    else:
        print("Invalid choice")

    return weigh

