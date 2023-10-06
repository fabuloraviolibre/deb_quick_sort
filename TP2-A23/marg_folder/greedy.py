from load_test_set import load_serie


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

    while bricks:

        #Choose the best next brick
        max_value, max_index = bricks[0], 0
        for i in range(len(bricks)):
            if volume(bricks[i]) > volume(max_value):
                max_value, max_index = bricks[i], i
        
        del(bricks[max_index])

        #Check if chosen brick can be on top of the tower
        if tower:
            if tower[-1][1] > max_value[1] and tower[-1][2] > max_value[2]:
                tower.append(max_value)
        else:
            tower.append(max_value)
        
    #Calculate the total height of the tower
    H = 0
    for brick in tower:
        H += brick[0]

    return tower, H


samples = load_serie(250)
tower, H = greedy(samples)