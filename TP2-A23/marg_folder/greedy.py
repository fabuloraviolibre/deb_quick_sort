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

    #Criteria: best volume
    sorted_bricks = sorted(bricks, key=volume, reverse=True)

    while sorted_bricks:

        #Choose the best next brick
        b = sorted_bricks[0]

        #The brick is no longer available
        del(sorted_bricks[0])

        #Check if chosen brick can be on top of the tower
        if tower:
            if tower[-1][1] > b[1] and tower[-1][2] > b[2]:
                tower.append(b)
        else:
            tower.append(b)

    return tower