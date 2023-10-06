import numpy as np
from load_exemple import load_gen 


def dynam_sort(tab: list) -> int:
    n = len(tab)
    h_tab = np.zeros(n, dtype=int)

    for i in range (n):
        h_tab[i] = tab[i][0]
        current_best = 0
        for j in range (i+1):
            if tab[j][1] > tab[i][1] and tab[j][2] > tab[i][2]:
                if h_tab[j] > current_best :
                    current_best = h_tab[j]
        h_tab[i] += current_best 

    return max(h_tab)



#complexité en O(n³) car O(n*somme(j=1, n))