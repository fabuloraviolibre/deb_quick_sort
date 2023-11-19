import numpy as np
from load_exemple import load_gen 
import time


######
#Programmation Dynamique
######


#trouve l'index du tableau ayant la hauteur la plus élévée
def find_max_index(tab):
    index = 0
    max = tab[0][0]
    n = len(tab)
    i = 1

    while i < n :
        if tab[i][0] > max :
            index = i
        i += 1

    return index

def dynam_sort(tab: list):
    n = len(tab)
    h_tab = np.zeros(n, dtype=tuple)

    for i in range (n):
        #pour chaque brique, on initialise le tableau avec la hauteur de la brique et son indice
        h_tab[i] = (tab[i][0], i)
        current_best_high = 0
        current_best_brick = i
        #si on trouve une brique j sur laquelle on peut empiler i, alors la nouvelle hauteure est h[i] + [j] et on note l'indice de la brique en dessous
        for j in range (i):
            if tab[j][1] > tab[i][1] and tab[j][2] > tab[i][2]:
                if h_tab[j][0] > current_best_high :
                    current_best_high = h_tab[j][0]
                    current_best_brick = j
        h_tab[i] = (h_tab[i][0] + current_best_high, current_best_brick)

    #permet de trouver la brique en haut de la tour
    index = find_max_index(h_tab)

    max_high = h_tab[index][0]
    tower = []

    parcourt = index 
    tower += [tab[parcourt]]
    #On remonte les indices pour trouver les briques les plus en bas de la tour
    while h_tab[parcourt][1] != parcourt :
        parcourt = h_tab[parcourt][1]
        tower += [tab[parcourt]]

    #on retourne la tour(par ordre décroissant de surface) et sa hauteur
    tower.reverse()

    return (tower, max_high)


for size in [250, 500, 750, 1000, 2500, 5000, 7500, 10000]:
    tab = load_gen(size,1)
    start = time.time()
    tower, max_high = dynam_sort(tab)
    end = time.time()
    print(f'h:{max_high}; time : {end-start}')

######
#Algorithme greedy
######

def volume(brick: list) -> float:
    """
    Args:
        brick (list): features (height, width, depth) of the brick
    Returns:
        float: volume
    """

    return brick[0]*brick[1]*brick[2]


def greedy(bricks: list) -> list:
    """
    Args:
        bricks (list): available bricks and their features (height, width, depth)
    Returns:
        list: sorted list
    """

    tower = []

    #Criteria: best volume
    sorted_bricks = sorted(bricks, key=volume, reverse=True)

    while sorted_bricks:

        #Choose the best next brick
        b = sorted_bricks[0]

        #The brick is no longer available
        del(sorted_bricks[0])

        #Check if chosen brick can be on top of the tower
        if tower:
            if tower[-1][1] > b[1] and tower[-1][2] > b[2]:
                tower.append(b)
        else:
            tower.append(b)

    return tower

######
#Algorithme probabilistique
######

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

######
#Traduit dans le bon format pour glouton et probabilistique 
######

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

def get_time_results(algo: str, serie: int) -> float:
    """
    Args:
        algo (str): 'greedy' or 'probabilistic'
        serie (int): size of the sample to use
    Returns:
        time (float): time of execution of the algorithm
    """
    
    sample = load_gen(serie, 1)
    t = 0.0

    if algo == 'glouton':
        start = time.time()
        greedy(sample)
        end = time.time()
    
    elif algo == 'proba':
        start = time.time()
        #5 loops to find the best solution
        tower = probabilistic(sample)
        for i in range(4):
            temp_tower = probabilistic(sample)
            if get_height(temp_tower) > get_height(tower):
                tower = temp_tower
        end = time.time()
    
    else:
        raise ValueError("Algorithm invalid")
    
    t = end - start
    return t

def get_results(algo: str, serie: int) -> (float, list):
    """
    Args:
        algo (str): 'greedy' or 'probabilistic'
        serie (int): size of the sample to use
    Returns:
        height (float): height of the tower
        tower (list): list of bricks to form the tower
    """
    
    sample = load_gen(serie, 1)
    h = 0.0

    if algo == 'glouton':
        tower = greedy(sample)
    
    elif algo == 'proba':
        #5 loops to find the best solution
        tower = probabilistic(sample)
        for i in range(4):
            temp_tower = probabilistic(sample)
            if get_height(temp_tower) > get_height(tower):
                tower = temp_tower
    
    else:
        raise ValueError("Algorithm invalid")
    
    h = get_height(tower)
    return h, tower
