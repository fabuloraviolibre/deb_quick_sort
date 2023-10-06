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
    print(tab)

perf_dynm(7500)
