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

        #Choose the best next brick (criteria: best volume)
        max_value, max_index = bricks[0], 0
        for i in range(len(bricks)):
            if volume(bricks[i]) > volume(max_value):
                max_value, max_index = bricks[i], i
        
        #The brick is no longer available
        del(bricks[max_index])

        #Check if chosen brick can be on top of the tower
        if tower:
            if tower[-1][1] > max_value[1] and tower[-1][2] > max_value[2]:
                tower.append(max_value)
        else:
            tower.append(max_value)

    return tower