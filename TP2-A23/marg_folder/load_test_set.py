import os

def load_serie(serie: int) -> list:
    """
    Args:
        serie(int): size of the serie to load
    Returns:
        list: samples of given size
    """

    samples = []

    f_names = os.listdir(f'./samples/serie_{serie}/')
    for name in f_names:
        with open(f'./samples/serie_{serie}/{name}', 'r') as f:
            bricks = [ [ int(feature) for feature in brick[:-1].split(' ') ] for brick in f.readlines() ]
    
    return bricks