import numpy as np
from load_exemple import load_gen 


def dynam_sort(tab: list) -> int:
    h = 0 
    n = len(tab)
    h_tab = np.zeros(n, dtype=int)

    for i in range (n):
        h_tab[i] = tab[i][0]
        current_best = 0
        for j in range (i):
            if tab[j][1] > tab[i][1] and tab[j][2] > tab[i][2]:
                if tab[j][0] > current_best :
                    current_best = tab[j][0]
        h_tab[i] += current_best 

    return max(h_tab)

list = load_gen(500, 2)
print(dynam_sort(list))


#complexité en O(n³) car O(n*somme(j=1, n))