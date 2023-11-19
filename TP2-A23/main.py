import time
import os
import argparse
from load_exemple import load_gen
import re

from sorts import dynam_sort, get_results, get_time_results

def load_examplaire(path: str) ->list:
    """
    Args:
        path(str): absolute path of the examplaire to load
    Returns:
        list: sorted examplaire
    """

    with open(path, 'r') as f:
        match = re.search(r'(\d+)_\d+\.txt', path)
        if match:
            size = int(match.group(1))

    return size



def compute_exemplaire(path: str, sort: str) ->float:
    """
    Args:
        serie(int): serie
        generation(int): generation of given serie
        sort(str): type of sorting
    Returns:
        float: mean duration of time execution
    """

    size = load_examplaire(path)

    if  size not in [250, 500, 1000, 2500, 5000, 7500, 10000] or sort not in ['glouton', 'progdyn', 'proba']:
        raise ValueError("Arguments not valid.")
    
    exemplaire = load_gen(size, 1)

    if sort == 'progdyn':
        start_time = time.time()
        tour, hauteur = dynam_sort(exemplaire)
        end_time = time.time()
        duration = (end_time - start_time)

    elif sort == 'glouton':
            hauteur, tour = get_results(sort, size)
            duration = get_time_results(sort, size)

    elif sort == 'proba':
            hauteur, tour = get_results(sort, size)
            duration = get_time_results(sort, size)

    return tour, hauteur, duration

if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--algorithm", required=True, type=str,
                        help="[counting | quick | quickSeuil | quickRandomSeuil]")
    parser.add_argument("-e", "--examplaire", required=True, type=str,
                        help="[path_vers_exemplaire]")
    parser.add_argument("-p", "--tour", required=False, action='store_true',
                        help="Affiche la tour construite, en partant de la brique du bas")
    parser.add_argument("-H", "--hauteur", required=False, action='store_true',
                        help="Affiche la hauteur de la tour")
    parser.add_argument("-t", "--time", required=False, action='store_true',
                        help="Affiche le temps d’exécution en ms")

    args = parser.parse_args()

    tour, hauteur, duration = compute_exemplaire(args.examplaire, args.algorithm)
    
    if args.tour:
        print('tour :', tour)
    if args.hauteur:
        print('hauteur :', hauteur)
    if args.time :
        print('temps de calcul :', duration)