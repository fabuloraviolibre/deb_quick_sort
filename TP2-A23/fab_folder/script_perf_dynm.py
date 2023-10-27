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

print(perf_dynm(500)[1])

