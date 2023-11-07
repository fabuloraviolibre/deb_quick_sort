from dynam_sort import dynam_sort
from load_exemple import load_gen 
import time

def perf_dynm(size: int):
    tab = []
    for i in range (1, 11):
        list = load_gen(size, i)
        start = time.time()
        h = dynam_sort(list)
        end = time.time()
        tab += [(h, end - start)]
    return tab

def mean_time_dynm(size):
    tab = perf_dynm(size)
    nb_ex = 0
    time = 0

    for perf in tab :
        nb_ex += 1
        time += perf[1]

    mean_time = time/nb_ex

    return mean_time


def max_hauteur(tab):
    max_ind = 0
    max = tab[max_ind][0][1]
    n = len(tab)

    i = 1
    while i < n :
        if tab[i][0][1] > tab[max_ind][0][1]:
            max = tab[i][0][1]
            max_ind = i
        i += 1

    return max, tab[max_ind]

def hauteur_time(size: int):
    tab = perf_dynm(size)
    max_h, tour = max_hauteur(tab)
    m_time = mean_time_dynm(size)
    print(f'{size} : ( hauteur max : {max_h}, time : {m_time}')
    print(tour, "\n")


for size in [250, 500, 750, 1000, 2500, 5000, 7500, 10000]:
   hauteur_time(size)



