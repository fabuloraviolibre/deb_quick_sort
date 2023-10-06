import os
"""
from greedy import greedy
from probabilistic import probabilistic
"""


def load_serie(serie: int) -> list:
    """
    Args:
        serie(int): size of the serie to load
    Returns:
        list: samples of given size
    """

    samples = []

    f_names = os.listdir(f'./samples/serie_{serie}/')
    for name in f_names:
        with open(f'./samples/serie_{serie}/{name}', 'r') as f:
            samples.append([ [ int(feature) for feature in brick[:-1].split(' ') ] for brick in f.readlines() ])
    
    return samples


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

"""
#Change the algorithm as you want
samples = load_serie(250)
for sample in samples:
    tower = probabilistic(sample)
    H = get_height(tower)
    print(H)
"""