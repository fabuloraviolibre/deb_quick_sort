import time

from load_test_set import load_gen
from sorts import counting_sort, quicksort_v1, quicksort_v2, quicksort_v3

def compute_time_execution(serie: int, generation: int, sort: str) ->float:
    """
    Args:
        serie(int): serie
        generation(int): generation of given serie
        sort(str): type of sorting
    Returns:
        duration(float): mean duration of time execution
    """

    if serie not in range(1,5) or generation not in range(1,5) or sort not in ['counting', 'quicksort_v1', 'quicksort_v2', 'quicksort_v3']:
        raise ValueError("Arguments not valid.")
    
    gen = load_gen(serie, generation)
    duration = 0.0

    if sort == 'counting':
        for sample in gen:
            start_time = time.time()
            counting_sort(sample)
            end_time = time.time()
            duration += (end_time - start_time)
    elif sort == 'quicksort_v1':
        for sample in gen:
            start_time = time.time()
            quicksort_v1(sample)
            end_time = time.time()
            duration += (end_time - start_time)
    elif sort == 'quicksort_v2':
        for sample in gen:
            start_time = time.time()
            quicksort_v2(sample)
            end_time = time.time()
            duration += (end_time - start_time)
    else:
        for sample in gen:
            start_time = time.time()
            quicksort_v3(sample)
            end_time = time.time()
            duration += (end_time - start_time)
    
    duration /= 10

    return duration


for i in range(1,5):
    t = compute_time_execution(1, i, 'counting')
    print(t)