
def swap(tab, i ,j):
    print(tab)
    val = tab[i]
    tab[i] = tab[j]
    tab[j] = val 

def tri_insertion(tab):
    return 2

def quick_sort_seuil(tab, seuil):
    n = len(tab)
    if n < seuil:
        #return tri_insertion(tab)
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
                


tab = [4, 5 ,9 , 4, 6, 8, 2, 1, 4, 9, 7, 3]

print(quick_sort_seuil(tab, 2))