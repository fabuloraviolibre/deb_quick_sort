import numpy as np
import random


def f(brick: list) -> float:
    """Criteria function: f(b_i) = Hauteur(b_i) + Aire_base(b_i)
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
    indexes = [i for i in range(len(bricks))]

    #Compute probabilities
    sum_exp = sum([np.exp(f(b)) for b in bricks])
    smx = [np.exp(f(b))/sum_exp for b in bricks]

    for k in range(len(bricks)):

        #Choose a brick
        i = random.choices(indexes, smx)[0]
        b = bricks[i]

        #Put the probability at 0.0
        smx[i] = 0.0

        #Check if chosen brick can be on top of the tower
        if tower:
            if tower[-1][1] > b[1] and tower[-1][2] > b[2]:
                tower.append(b)
        else:
            tower.append(b)
    
    return tower