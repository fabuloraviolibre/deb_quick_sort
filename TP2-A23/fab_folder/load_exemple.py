import os

def sort_key(item):
    return item[1] * item[2]


def load_gen(size: int, nb_ex: int) ->list:
    """
    Args:
        serie(int): index of the serie's generation to load
        gen(int): index of the generation to load
    Returns:
        list: list (generation) of lists(samples)
    """

    if nb_ex in range(1,11):
        #file_names = os.listdir(f'./samples/sample_{size}_{nb_ex}.txt')
        generation = []
        #for name in file_names:
        with open(f'./samples/sample_{size}_{nb_ex}.txt', 'r') as f:
            for line in f:
                h, l, p= line.split(' ')
                generation += [(int(h), int(l), int(p))]
            #del(l[-1])
            #l = [int(val) for val in l]
            #generation.append(l)
        sorted_generation = sorted(generation, key=sort_key, reverse=True)
        return sorted_generation
    
    else:
        raise ValueError("serie and gen have to be in range(1,5).")
    
(load_gen(500, 2))