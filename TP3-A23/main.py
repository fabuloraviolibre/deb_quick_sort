import random
import argparse
import numpy as np


def load_sample(path: str) ->dict:
    """
    Args:
        path (str): path of the sample to load
    Returns:
        sample (dict): n_pupils (int): number of number of pupils,
                       n_pairs (int): number of pairs to avoid,
                       sizes (list): pupils' sizes,
                       pairs (list): pairs to avoid
    """

    with open(path, 'r') as f:
        lines = [line[:-1] for line in f.readlines()]
        sample = {'n_pupils': int(lines[0]),
                  'n_pairs': int(lines[1]),
                  'sizes': [],
                  'pairs': [],
                  }
        sample['sizes'] = [int(size) for size in lines[2 : 2+sample['n_pupils']]]
        sample['pairs'] = [[int(pair.split()[0]), int(pair.split()[1])] for pair in lines[2+sample['n_pupils'] :]]
        return sample
    

# NB : code repris de check_sol fourni par le professeur
def get_matrixes(sizes, pairs):
        sM = (np.array(sizes)[:, np.newaxis] >= sizes)
        n = len(sizes)
        pM = np.zeros((n,n))
        pairs = pairs + [p[::-1] for p in pairs]
        for p in pairs:
            pM[p] = 1
        return sM, pM


# NB : code repris (et légèrement adapté) de check_sol fourni par le professeur
def compute_loss(sample: dict, line: list) -> float:
    """Compute loss given by écoliers obstrués + 10*(paires d’écoliers se chamaillant)
    Args:
        sample (dict): sample
        line (list): line returned by an algorithm (from behind to front)
    Returns:
        loss (float): loss
    """

    pairs = list(map(tuple,sample['pairs']))
    sM , pM = get_matrixes(sample['sizes'], pairs)
    loss = 0; n_a = 0
    tallest = sample['sizes'][line[0]]
    for i in range(1, sM.shape[0]):
        size = sample['sizes'][line[i]]
        if size >= tallest:
            tallest = size
        else:
            loss += 1
        
        n_a += pM[line[i-1], line[i]]
    return loss + 10*int(n_a)


def algorithm(path: str, print_sol: bool) -> (int, list):
    """Main function: our optimization algorithm
    Args:
        sample (dict): sample of pupils to align
    Returns:
        loss (int): final loss
        line (list): final line
    """

    # Load the sample
    sample = load_sample(path)

    """First configuration"""

    # Initial line: pupils sorted by size
    line = [x[0] for x in sorted([(i, sample['sizes'][i]) for i in range(sample['n_pupils'])], key=lambda x: x[1])]

    # Go through the list to reduce the number of impossible pairs
    for i in range(1, sample['n_pupils']):

        # For each pupil who pauses a problem, try to deplace them
        if [line[i-1], line[i]] in sample['pairs'] or [line[i], line[i-1]] in sample['pairs']:
            j = i+1

            while j-i < 10 and j < sample['n_pupils']:
                if [line[i-1], line[j]] in sample['pairs'] or [line[j], line[i-1]] in sample['pairs']\
                or [line[j-1], line[i]] in sample['pairs'] or [line[i], line[j-1]] in sample['pairs']:
                    j += 1
                elif j < sample['n_pupils']-1 and ([line[j+1], line[i]] in sample['pairs'] or [line[i], line[j+1]] in sample['pairs']):
                    j += 1
                else:
                    line[i], line[j] = line[j], line[i]
                    break
    
    loss = compute_loss(sample, line)

    # Print either the current solution or its loss
    if print_sol:
        print(' '.join(map(str, line)), flush=True)
    else:
        print(loss, flush=True)
    
    """Try permutations to improve the configuration
    Example of losses before: 15, 6, 96, 0, 111
    Examples of losses after: 4, 6, 50, 0, 108"""

    max_iter = 10**6

    while max_iter > 0 and loss > 0:
        i, j = random.choices([i for i in range(sample['n_pupils'])], k=2)

        tmp_line = line.copy()
        tmp_line[i], tmp_line[j] = tmp_line[j], tmp_line[i]
        tmp_loss = compute_loss(sample, tmp_line)

        # Update the line if we get a better configuration
        if tmp_loss < loss:
            line[i], line[j] = line[j], line[i]
            loss = tmp_loss
            # Print either the current solution or its loss
            if print_sol:
                print(' '.join(map(str, line)), flush=True)
            else:
                print(loss, flush=True)

        max_iter -= 1

    return loss, line


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--examplaire", required=True, type=str,
                        help="[path_vers_exemplaire]")
    parser.add_argument("-p", "--print_solution", required=False, action='store_true',
                        help="Affiche la nouvelle solution trouvée, en partant du premier rang")
    args = parser.parse_args()

    loss, line = algorithm(args.examplaire, args.print_solution)