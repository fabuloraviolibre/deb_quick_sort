import os
from time import time
import matplotlib.pyplot as plt

from greedy import greedy
from probabilistic import probabilistic


def load_serie(serie: int) -> list:
    """
    Args:
        serie(int): size of the serie to load
    Returns:
        list: samples of given size
    """

    with open(f'./samples/sample_{serie}_1.txt', 'r') as f:
        sample = [ [ int(feature) for feature in brick[:-1].split(' ') ] for brick in f.readlines() ]
    
    return sample


def get_height(tower: list) -> float:
    """
    Args:
        tower (list): bricks obtained with any algorithm
    Returns:
        float: height of the tower
    """

    H = 0
    for brick in tower:
        H += brick[0]

    return H


def get_results(algo: str, serie: int) -> (float, float):
    """
    Args:
        algo (str): 'greedy' or 'probabilistic'
        serie (int): size of the sample to use
    Returns:
        height (float): height of the tower
        time (float): time of execution of the algorithm
    """
    
    sample = load_serie(serie)
    h, t = 0.0, 0.0

    if algo == 'greedy':
        start = time()
        tower = greedy(sample)
        end = time()
    
    elif algo == 'probabilistic':
        start = time()
        #5 loops to find the best solution
        tower = probabilistic(sample)
        for i in range(4):
            temp_tower = probabilistic(sample)
            if get_height(temp_tower) > get_height(tower):
                tower = temp_tower
        end = time()
    
    else:
        raise ValueError("Algorithm invalid")
    
    t = end - start
    h = get_height(tower)

    return h,t


def plot_perf_probabilistic():
    """Plot height/optimal_height in function of the number of iterations of the algorithm"""

    sample = load_serie(10000)
    h_optimal = 389

    heights = []
    iterations = [n for n in range(1, 101)]

    for n in iterations:

        h = get_height(probabilistic(sample))

        for i in range(1,n):
            temp_h = get_height(probabilistic(sample))
            if temp_h > h:
                h = temp_h
        
        heights.append(h/h_optimal)

        print(f'Iteration {n}/100 : the best height is {h}.')

    
    plt.clf()
    plt.plot(iterations, heights)
    plt.xlabel('Iterations')
    plt.ylabel('Height')
    plt.legend()
    plt.title('Evolution du rapport (Hauteur atteinte) / (Hauteur optimale)')
    plt.show()


plot_perf_probabilistic()