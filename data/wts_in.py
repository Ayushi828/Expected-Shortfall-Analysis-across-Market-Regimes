
weight = []

def wt_distribution():
   
    for w in range(1,11):
        w = float(input(f"weight for stock{w} : \t" ))
        weight.append(w)

    return weight
