import time
import os
import argparse

from sorts import counting_sort, quicksort_v1, quicksort_v2, quicksort_v3


def load_gen(serie: int, gen: int) ->list:
    """
    Args:
        serie(int): index of the serie's generation to load
        gen(int): index of the generation to load
    Returns:
        list: list (generation) of lists(samples)
    """

    if serie in range(1,5) and gen in range(1,5):
        file_names = os.listdir(f'./samples/serie{serie}/gen{gen}/')
        generation = []
        for name in file_names:
            with open(f'./samples/serie{serie}/gen{gen}/{name}', 'r') as f:
                l = f.read().split(' ')
                del(l[-1])
                l = [int(val) for val in l]
                generation.append(l)
        return generation
    
    else:
        raise ValueError("serie and gen have to be in range(1,5).")


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


def compute_time_gen(serie: int, generation: int, sort: str) ->float:
    """
    Args:
        serie(int): serie
        generation(int): generation of given serie
        sort(str): type of sorting
    Returns:
        float: mean duration of time execution
    """

    if serie not in range(1,5) or generation not in range(1,5) or sort not in ['counting', 'quick', 'quickSeuil', 'quickRandomSeuil']:
        raise ValueError("Arguments not valid.")
    
    gen = load_gen(serie, generation)
    duration = 0.0

    if sort == 'counting':
        for sample in gen:
            start_time = time.time()
            counting_sort(sample)
            end_time = time.time()
            duration += (end_time - start_time)

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
    
    duration /= 10

    return duration


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
    parser.add_argument("-p", "--print", required=False, action='store_true',
                        help="Affiche les nombres triés en ordre croissant sur une ligne, sans texte superflu")
    parser.add_argument("-t", "--time", required=False, action='store_true',
                        help="Affiche le temps d’exécution en ms, sans unité ni texte superflu")

    args = parser.parse_args()

    (sample, duration) = compute_time_examplaire(args.examplaire, args.algorithm)
    
    if args.print:
        for k in sample:
            print(k, end=' ')
        print('')
    if args.time:
        print(duration)