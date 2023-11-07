from matplotlib import pyplot as plt
from dynam_sort import dynam_sort
from load_exemple import load_gen 
from script_perf_dynm import mean_time_dynm
import numpy as np
from sklearn.linear_model import LinearRegression

sample = np.array([250, 500, 750, 1000, 2500, 5000, 7500, 10000])

y = np.empty(8, dtype='float')

i = 0
nb_test = len(sample)

while i < nb_test:
    print(i)
    y[i] = mean_time_dynm(sample[i])
    print(y[i])
    i += 1


log_sample = np.log(sample)
log_y = np.log(y)

model = LinearRegression()

model.fit(log_sample.reshape(-1, 1), log_y)

slope = model.coef_[0]

plt.plot(log_sample, log_y, label=f"Regression Line (Slope: {slope:.2f})", color="r")
plt.xlabel('size')
plt.ylabel('time')
plt.title(f'Test puissance algo dynamique')
plt.savefig(f'./tests/puissance_algo_dynamique.png')
plt.show()

