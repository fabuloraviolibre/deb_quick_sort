from matplotlib import pyplot as plt
from dynam_sort import dynam_sort
from load_exemple import load_gen 
from script_perf_dynm import mean_time_dynm
import numpy as np

sample = np.array([250, 500, 750, 1000, 2500, 5000, 7500, 10000])

y = np.empty(8, dtype='int')

i = 0
nb_test = len(sample)

while i < nb_test:
    print(i)
    y[i] = mean_time_dynm(sample[i])
    i += 1


plt.plot(np.log(sample), np.log(y), marker='o')
plt.xlabel('size')
plt.ylabel('time')
plt.title(f'Test puissance algo dynamique')
plt.savefig(f'./tests/puissance_algo_dynamique.png')
plt.show()

coefficients = np.polyfit(np.log(sample), np.log(y), 1)
print(coefficients[0])
