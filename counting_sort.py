import numpy as np

def counting_sort(tab, mag):
    n = len(tab)
    sorted_tab = np.zeros(n, dtype=np.int64)
    frequence_tab = np.zeros(mag, dtype=np.int64)
    for k in tab:
        frequence_tab[k] += 1
    ind = 0
    while ind < n:
        for k in range(mag):
            if frequence_tab[k] != 0:
                for j in range(frequence_tab[k]):
                    sorted_tab[ind] = k
                    ind += 1
    return(sorted_tab)



