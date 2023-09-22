"""
This script aims to show how we chose the thresholds of quicksort_v2 and quicksort-v3. We apply the trial and error method
To compute time execution, we chose the serie 1 - generation 2 (size: 10000, magnitude:1000000).
"""

import time
import matplotlib.pyplot as plt

from load_test_set import load_gen
from sorts import quicksort_v2, quicksort_v3

gen = load_gen(1,4)
thresholds = [i for i in range(1, 10000)]


"""Threshold of quicksort_v2"""

mean_durations = []

for t in thresholds:
    duration = 0.0
    for sample in gen:
        start_time = time.time()
        quicksort_v2(sample, t)
        end_time = time.time()
        duration += (end_time - start_time)
    mean_durations.append(duration/10)

best_threshold = mean_durations.index(min(mean_durations)) + 1
print(best_threshold)

plt.clf()
plt.plot(thresholds, mean_durations)
plt.xlabel('Thresholds')
plt.ylabel('Time execution')
plt.title('Time execution according to thresholds (quicksort_v2)')
plt.show()


"""Threshold of quicksort_v3

mean_durations = []

for t in thresholds:
    duration = 0.0
    for sample in gen:
        start_time = time.time()
        quicksort_v3(sample, t)
        end_time = time.time()
        duration += (end_time - start_time)
    mean_durations.append(duration/10)

best_threshold = mean_durations.index(min(mean_durations)) + 1
print(best_threshold)

plt.clf()
plt.plot(thresholds, mean_durations)
plt.xlabel('Thresholds')
plt.ylabel('Time execution')
plt.title('Time execution according to thresholds (quicksort_v3)')
plt.show()

"""