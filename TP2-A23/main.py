import time
import os
import argparse
from load_exemple import load_gen

from sorts import dynam_sort, greedy, proba

def load_examplaire(path: str) ->list:
    """
    Args:
        path(str): absolute path of the examplaire to load
    Returns:
        list: sorted examplaire
    """

    with open(path, 'r') as f:
        l = f.read().split(' ')
        del(l[-1])
        l = [int(val) for val in l]
    return l


def compute_exemplaire(path: str, sort: str) ->float:
    """
    Args:
        serie(int): serie
        generation(int): generation of given serie
        sort(str): type of sorting
    Returns:
        float: mean duration of time execution
    """

    size, serie = load_examplaire(path)

    if serie not in range(1,11) or size not in [250, 500, 1000, 2500, 5000, 7500, 10000] or sort not in ['glouton', 'progdyn', 'proba']:
        raise ValueError("Arguments not valid.")
    
    exemplaire = load_gen(size, serie)

    if sort == 'progdyn':
        start_time = time.time()
        tour, hauteur = dynam_sort(exemplaire)
        end_time = time.time()
        duration = (end_time - start_time)

    return tour, hauteur, duration
"""
    elif sort == 'quick':
        for sample in gen:
            start_time = time.time()
            quicksort_v1(sample)
            end_time = time.time()
            duration += (end_time - start_time)

    elif sort == 'quickSeuil':
        for sample in gen:
            start_time = time.time()
            quicksort_v2(sample)
            end_time = time.time()
            duration += (end_time - start_time)

    else:
        for sample in gen:
            start_time = time.time()
            quicksort_v3(sample)
            end_time = time.time()
            duration += (end_time - start_time)
"""  



def compute_time_examplaire(path: str, sort: str) ->float:
    """
    Args:
        path(str): absolute path of the examplaire to sort
        sort(str): type of sorting
    Returns:
        list: sorted examplaire
        float: mean duration of time execution
    """

    if sort not in ['counting', 'quick', 'quickSeuil', 'quickRandomSeuil']:
        raise ValueError("Arguments not valid.")
    
    sample = load_examplaire(path)

    if sort == 'counting':
        start_time = time.time()
        sample = counting_sort(sample)
        end_time = time.time()
        duration = (end_time - start_time)

    elif sort == 'quick':
        start_time = time.time()
        quicksort_v1(sample)
        end_time = time.time()
        duration = (end_time - start_time)

    elif sort == 'quickSeuil':
        start_time = time.time()
        quicksort_v2(sample)
        end_time = time.time()
        duration = (end_time - start_time)

    else:
        start_time = time.time()
        quicksort_v3(sample)
        end_time = time.time()
        duration = (end_time - start_time)

    return sample, duration



if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--algorithm", required=True, type=str,
                        help="[counting | quick | quickSeuil | quickRandomSeuil]")
    parser.add_argument("-e", "--examplaire", required=True, type=str,
                        help="[path_vers_exemplaire]")
    parser.add_argument("-p", "--tour", required=False, action='store_true',
                        help="Affiche la tour construite, en partant de la brique du bas")
    parser.add_argument("-h", "--hauteur", required=False, action='store_true',
                        help="Affiche la hauteur de la tour")
    parser.add_argument("-t", "--time", required=False, action='store_true',
                        help="Affiche le temps d’exécution en ms")

    args = parser.parse_args()

    tour, hauteur, duration = compute_exemplaire(args.examplaire, args.algorithm)
    
    if args.tour:
        print(tour, end=' ')
        print("\n")
    if args.hauteur:
        print(hauteur)
        print("\n")
    if args.time :
        print(duration)