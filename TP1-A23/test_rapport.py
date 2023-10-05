import numpy as np
import matplotlib.pyplot as plt

def square(x):
    return x**2

square_table_1 = list(map(square, np.array([[50000], [100000], [200000], [400000]])))
square_table_2 = list(map(square, np.array([[500000], [1000000], [2000000], [4000000]])))
square_table_3 = list(map(square, np.array([[50000, 500000], [100000, 1000000], [200000, 2000000], [400000, 4000000]])))
square_table_4 = list(map(square, np.array([[50000], [100000], [200000], [400000]])))

samples = {
    'x_1': square_table_1,
    'x_2': square_table_2,
    'x_3': square_table_3,
    'x_4': square_table_4,
    'y_counting_1': np.array([[145.99], [199.29], [268.05], [383.12]]),
    'y_counting_2': np.array([[85.43], [141.28], [279.83], [691.00]]),
    'y_counting_3': np.array([[88.82], [186.74], [352.76], [802.74]]),
    'y_quick_1': np.array([[81.90], [181.71], [416.41], [1088.59]]),
    'y_quick_4': np.array([[136.22], [307.86], [674.91], [1481.40]]),
    'y_quickSeuil_1': np.array([[66.45], [141.97], [326.44], [768.64]]),
    'y_quickSeuil_4': np.array([[113.74], [339.12], [593.38], [1371.91]]),
    'y_quickSeuilRandom_1': np.array([[70.93], [150.68], [369.08], [770.22]]),
    'y_quickSeuilRandom_4': np.array([[59.21], [133.72], [297.01], [699.51]]),
}

def test_rapport(algo: str, i: int):
    """Display and save graph
    Args:
        algo(str): [ counting | quick | quickSeuil |quickSeuilRandom ]
        i(int): number of the serie
    """
    
    x = samples[f'x_{i}']
    y = samples[f'y_{algo}_{i}']
    
    plt.plot(x, y, marker='o')
    #plt.xscale('log')
    #plt.yscale('log')
    plt.xlabel('size')
    plt.ylabel('time')
    plt.title(f'Test rapport {algo} série {i}')
    plt.savefig(f'TP1-A23/tests/rapport/{algo}_serie{i}.png')
    plt.show()