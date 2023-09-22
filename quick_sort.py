import matplotlib.pyplot as plt
import time
import numpy as np
import load_test_set


def swap(tab, i ,j):
    val = tab[i]
    tab[i] = tab[j]
    tab[j] = val 

def tri_insertion(tab):
    n = len(tab)
    k = 1
    while k < n:
        i = k
        j = i - 1
        while i > 0 and tab[j] > tab[i]:
            swap(tab,i ,j)
            i = j
            j = i - 1
        k += 1

def quick_sort_seuil(tab, seuil):
    n = len(tab)
    if n <= seuil:
        tri_insertion(tab)
        return tab
    else:
        p = 0
        val_p = tab[p]
        i = 0
        j = 1
        while j < n:
            if tab[j] < val_p:
                i += 1
                swap(tab,i, j)
                j +=1
            else:
                j += 1
        swap(tab, p, i)
        p = i
    return (quick_sort_seuil(tab[:p],seuil) + [tab[p]] + quick_sort_seuil(tab[p+1:], seuil))
                

def plot_time_quick_seuil(tab):
    time_tab = []

    for seuil in range(100):
        start = time.time()
        quick_sort_seuil(tab, seuil)
        end = time.time()
        time_tab.append(end - start)

    plt.plot(np.arange(0, 100, dtype = int), time_tab, 'o-')

    plt.xlabel('seuil')
    plt.ylabel('temps éxécution')
    plt.title('beau gosse')

    plt.show()


'''
tab = [4, 5 ,9 , 4, 6, 8, 2, 1, 4, 9, 7, 3]

print(tri_insertion(tab))
print(quick_sort_seuil(tab, 38))

gen = load_test_set.load_gen(3, 4)

plot_time_quick_seuil(gen[2])
'''



gen = load_test_set.load_gen(1,4)
thresholds = [i for i in range(10, 100)]


"""Threshold of quicksort_v2"""
print("jésus")
mean_durations = []

for t in thresholds:
    print(t)
    duration = 0.0
    for sample in gen:
        zombie_sample = sample
        start_time = time.time()
        quick_sort_seuil(zombie_sample, t)
        end_time = time.time()
        duration += (end_time - start_time)
    mean_durations.append(duration/10)

best_threshold = mean_durations.index(min(mean_durations)) + 1
print(best_threshold)

plt.clf()
plt.plot(thresholds, mean_durations)
plt.xlabel('Thresholds')
plt.ylabel('Time execution')
plt.title('Time execution according to thresholds (quicksort_v2)')
plt.show()