from load_exemple import load_gen
import numpy as np

def swap(tab, i, j):
    v = tab[i]
    tab[i] = tab[j]
    tab[j] = v

def sort_tab_with_index(tab):
    i = 0
    n = len(tab)

    sorted_tab_with_index = np.empty(n, dtype="object")

    while i < n :
        ind_min = i 
        min = tab[i]
        for j in range(i+1, n):
            if tab[j] < min :
                min = tab[j]
                ind_min = j
        swap(tab, i, ind_min)
        sorted_tab_with_index[i] = (ind_min, min)
        i += 1

    return sorted_tab_with_index

#On défini deux scores :
#
#   -Un proportionnel à la taille ET au niveau de "turbulence" (un élève est d'autant plus
# turbulent qu'il se chamaille avec beaucoup d'élève)
#    -Un proportionnel à la taille DIVISER par le niveau de chamaillerie ( les élèves "tranquilles")
#
#Le but est ensuite d'altérner un élève du tableau des "turbulents" avec un du tableau
#des "tranquilles"

def glouton_criteria(nb_students, height_tab, pair_tab):
    chamaille_tab = np.zeros(nb_students, dtype="int")
    student_turbulent_tab = np.empty(nb_students, dtype="float")
    student_chill_tab = np.empty(nb_students, dtype="float")

    for pair in pair_tab :
        chamaille_tab[pair[0]] += 1
        chamaille_tab[pair[1]] += 1

    max_turb = max(chamaille_tab)
    max_height = max(height_tab)
  
    for i in range(nb_students):
        student_turbulent_tab[i] = (height_tab[i]/max_height) * (chamaille_tab[i]/max_turb)
        student_chill_tab[i] = (height_tab[i]/max_height) / (chamaille_tab[i]/max_turb)
    
    student_turbulent_tab = sort_tab_with_index(student_turbulent_tab)
    student_chill_tab = sort_tab_with_index(student_chill_tab)

    return student_turbulent_tab, student_chill_tab

#test score

height_tab, pair_tab = load_gen(10, 25)
student_turbulent_tab, student_chill_tab = glouton_criteria(10, height_tab, pair_tab)
print(student_turbulent_tab)
print(student_chill_tab)

#end test score        


def making_rang(nb_students : int, nb_pairs : int):
    height_tab, pair_tab = load_gen(nb_students, nb_pairs)
    student_turbulent_tab, student_chill_tab = glouton_criteria(nb_students, height_tab, pair_tab)
    rang = np.empty(nb_students, dtype="int")

    for i in range(nb_students-1):
        rang[i] = student_turbulent_tab[i][0]
        rang[i+1] = student_chill_tab[i][0]

    return rang





###Calcul Score###

def obstruction(rang_soluce, height_tab):
    score = 0
    n = len(rang_soluce)

    for i in range(n):
        j = i+1
        obs = 0
        while j < n and obs != 1:
            if height_tab[j] > height_tab[i]:
                obs = 1
            j += 1
        if obs == 1:
            score += 1

    return score

def chamaillage(rang_soluce, pair_tab):
    score = 0
    n = len(rang_soluce)

    for i in range(n):
        if (rang_soluce[i], rang_soluce[i+1]) in pair_tab :
            score += 10

    return score


def score(rang_soluce, height_tab, pair_tab):
    return obstruction(rang_soluce, height_tab) + chamaillage(rang_soluce, pair_tab)