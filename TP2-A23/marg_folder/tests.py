import matplotlib.pyplot as plt
import numpy as np


x = [250, 500, 750, 1000, 2500, 5000, 7500, 10000]
y_greedy = [0.00008965, 0.0001950, 0.0002785, 0.0004823, 0.001208, 0.004545, 0.009969, 0.01387]
y_prob = [0.03644, 0.09243, 0.1997, 0.3100, 1.778, 6.666, 15.15, 30.69]


def test_puissance(x: list, y: list, m=2):
    """
    Args:
        x (list): sizes
        y (list): execution times
    """

    plt.clf()
    log_x = [np.log(k) for k in x]
    log_y = [m*np.log(k) for k in y]
    plt.plot(log_x, log_y, marker='o')
    plt.xlabel('sample size')
    plt.ylabel('rapport')
    plt.title('Test de puissance')
    plt.show()

def test_rapport(x: list, y: list, m=2):
    """
    Args:
        x (list): sizes
        y (list): execution times
    """

    plt.clf()
    rapport = [y[i]/x[i]**m for i in range(len(x))]
    plt.plot(x, rapport, marker='o')
    plt.xlabel('sample size')
    plt.ylabel('rapport')
    plt.title('Test de rapport')
    plt.show()