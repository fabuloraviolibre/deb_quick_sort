import os

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