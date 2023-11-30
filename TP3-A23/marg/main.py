from itertools import permutations
import time


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
    

def compute_true_sol(sample: dict) -> (int, list):
    """Compute the true solution by generating and testing
    Args:
        sample (dict): sample to test
    Returns:
        val_opt (int): loss of optimal line
        line_opt (list): optimal line
    """

    pupils = [i for i in range(sample['n_pupils'])]
    all_permutations = [list(perm) for perm in list(permutations(pupils))]
    line_opt = pupils
    val_opt = compute_loss(sample, line_opt)

    for perm in all_permutations:
        loss = compute_loss(sample, perm)
        if loss < val_opt:
            val_opt = loss
            line_opt = perm
    
    return val_opt, line_opt


def compute_loss(sample: dict, line: list) -> float:
    """Compute loss given by écoliers obstrués + 10*(paires d’écoliers se chamaillant)
    Args:
        sample (dict): sample
        line (list): line returned by an algorithm (from behind to front)
    Returns:
        loss (float): loss
    """

    obstructed_pupils = 0
    problematic_pairs = 0
    n = len(line)

    for i in range(n-1):

        # Compute problematic_pairs
        if [line[i], line[i+1]] in sample['pairs'] or [line[i+1], line[i]] in sample['pairs']:
            problematic_pairs += 1

        # Compute obstructed_pupils
        for j in range(i+1, n):
            if sample['sizes'][line[j]] > sample['sizes'][line[i]]:
                obstructed_pupils += 1
                break
    
    loss = obstructed_pupils + 10*problematic_pairs
    return loss


def sort_first(sample: dict) -> (int, list):
    """
    Args:
        sample (dict): sample of pupils to align
    Returns:
        loss (int): loss of the returned line
        line (list): line
    """

    line = [(i, sample['sizes'][i]) for i in range(sample['n_pupils'])]
    
    # First: sort the line by size
    line = [x[0] for x in sorted(line, key=lambda x: x[1], reverse=True)]
    
    for i in range(1, sample['n_pupils']):

        # For each pupil who pauses a problem, try to deplace them
        if [line[i-1], line[i]] in sample['pairs'] or [line[i], line[i-1]] in sample['pairs']:
            j = i+1

            while j <= i+10 and j < sample['n_pupils']:
                if [line[i-1], line[j]] in sample['pairs'] or [line[j], line[i-1]] in sample['pairs']\
                or [line[j-1], line[i]] in sample['pairs'] or [line[i], line[j-1]] in sample['pairs']:
                    j += 1
                elif j < sample['n_pupils']-1 and ([line[j+1], line[i]] in sample['pairs'] or [line[i], line[j+1]] in sample['pairs']):
                    j += 1
                else:
                    line[i], line[j] = line[j], line[i]
                    break
    
    loss = compute_loss(sample, line)
    return loss, line



paths = ["/home/margot/Cours EPM/INF8775 - Conception et Analyse d'Algorithme/TPs/TP3-A23/samples/sample_10_25_1.txt",
         "/home/margot/Cours EPM/INF8775 - Conception et Analyse d'Algorithme/TPs/TP3-A23/samples/sample_60_300_1.txt",
         "/home/margot/Cours EPM/INF8775 - Conception et Analyse d'Algorithme/TPs/TP3-A23/samples/sample_60_1000_1.txt",
         "/home/margot/Cours EPM/INF8775 - Conception et Analyse d'Algorithme/TPs/TP3-A23/samples/sample_400_1000_1.txt",
         "/home/margot/Cours EPM/INF8775 - Conception et Analyse d'Algorithme/TPs/TP3-A23/samples/sample_400_20000_1.txt"]

for path in paths:
    # Load the sample and the pupils
    sample = load_sample(path)

    # Compute the time of execution
    start_time = time.time()
    loss, line = sort_first(sample)
    end_time = time.time()
    t = end_time - start_time

    print('Sample:', path)
    print('Execution time:', t)
    # print('Line:', line)
    print('Loss:', loss, '\n')

"""
print('For the first sample:')
sample = load_sample("/home/margot/Cours EPM/INF8775 - Conception et Analyse d'Algorithme/TPs/TP3-A23/samples/sample_10_25_1.txt")
true_loss, true_line = compute_true_sol(sample)
print(true_loss)
print(true_line)

Affiche :
For the first sample:
4
[0, 6, 7, 4, 5, 9, 8, 1, 2, 3]

Donc algorithme non optimal
"""