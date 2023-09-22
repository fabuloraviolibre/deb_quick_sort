import time
import numpy as np

from load_test_set import load_gen
from sorts import counting_sort, insertion_sort, quicksort_v1, quicksort_v2, quicksort_v3


def check_order(l: list):
    for i in range(1,len(l)):
        if l[i] < l[i-1]:
            print(f'Not good. l[{i}]: {l[i]} and l[{i-1}]: {l[i-1]}')
            return False
    print('Ok.')
    return True


l = load_gen(1, 1)[0]
print('Avant:\n', l[:10])
insertion_sort(l, 0, len(l)-1)
print('Après:\n', l[:10])
check_order(l)