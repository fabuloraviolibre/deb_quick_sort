import numpy as np


def f(brick: list) -> float:
    """Softmax function: f(bi) = Hauteur(bi) + Aire_base(bi)
    Args:
        brick (list): features (height, width, depth) of the brick
    Returns:
        float: result of softmax function
    """

    return brick[0] + brick[1]*brick[2]


def probabilistic(bricks: list) -> list:
    """
    Args:
        bricks (list): available bricks and their features (height, width, depth)
    Returns:
        list: sorted list
    """

    tower = []

    fitnesses = sorted(bricks, key=f, reverse=True)
    s = sum([ np.exp(f(b)) for b in fitnesses ])
    probabilities = [ np.exp(f(b))/s for b in fitnesses ]

    for i in range(len(fitnesses)):
        chosen_brick = np.random.choice(fitnesses, p=probabilities)
        
        

    """
    tower.append(max_value)
    probabilities.remove(max_value)
    """

    return tower


from main import load_serie
samples = load_serie(250)
probabilistic(samples[0])