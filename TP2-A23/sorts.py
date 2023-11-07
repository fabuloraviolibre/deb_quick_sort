import numpy as np
from load_exemple import load_gen 


######
#Programmation Dynamique
######


#trouve l'index du tableau ayant la hauteur la plus élévée
def find_max_index(tab):
    index = 0
    max = tab[0][0]
    n = len(tab)
    i = 1

    while i < n :
        if tab[i][0] > max :
            index = i
        i += 1

    return index

def dynam_sort(tab: list) -> int:
    n = len(tab)
    h_tab = np.zeros(n, dtype=tuple)

    for i in range (n):
        #pour chaque brique, on initialise le tableau avec la hauteur de la brique et son indice
        h_tab[i] = (tab[i][0], i)
        current_best_high = 0
        current_best_brick = i
        #si on trouve une brique j sur laquelle on peut empiler i, alors la nouvelle hauteure est h[i] + [j] et on note l'indice de la brique en dessous
        for j in range (i):
            if tab[j][1] > tab[i][1] and tab[j][2] > tab[i][2]:
                if h_tab[j][0] > current_best_high :
                    current_best_high = h_tab[j][0]
                    current_best_brick = j
        h_tab[i] = (h_tab[i][0] + current_best_high, current_best_brick)

    #permet de trouver la brique en haut de la tour
    index = find_max_index(h_tab)

    max_high = h_tab[index][0]
    tower = []

    parcourt = index 
    tower += [tab[parcourt]]
    #On remonte les indices pour trouver les briques les plus en bas de la tour
    while h_tab[parcourt][1] != parcourt :
        parcourt = h_tab[parcourt][1]
        tower += [tab[parcourt]]

    #on retourne la tour(par ordre décroissant de surface) et sa hauteur
    return (tower.reverse(), max_high)