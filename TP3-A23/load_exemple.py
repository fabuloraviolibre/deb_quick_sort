import os
import numpy as np 

def load_gen(nb_students: int, nb_pairs: int) ->list:
    """
    Args:
        nb students(int)
        nb pairs(int)
    """

    height_tab = np.empty(nb_students, dtype="int")
    pair_tab = np.empty(nb_pairs, dtype="object")

    with open(f'./samples/sample_{nb_students}_{nb_pairs}_1.txt', 'r') as f:
        #skip first two lines 
        f.readline()
        f.readline()
        
        pupil = 0
      
        while pupil < nb_students:
            height = int(f.readline())
            height_tab[pupil] = height
            pupil += 1

        pair = 0

        while pair < nb_pairs:
            student_1, student_2 = f.readline()[:-1].split(' ')
            pair_tab[pair] = (int(student_1), int(student_2))
            pair += 1

    return height_tab, pair_tab
    