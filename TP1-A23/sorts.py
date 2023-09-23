from random import randint


"""--------------------------- Counting sort ---------------------------"""

def counting_sort(l: list) ->list:
    """
    Args:
        l(list): list to sort
    Returns:
        list: l sorted by counting sort
    """

    N = len(l)
    M = max(l)
    sorted_list = [0 for i in range(N)]
    temp_list = [0 for i in range(M+1)]

    for i in range(N):
        temp_list[l[i]] += 1
    
    for i in range(1, M+1):
        temp_list[i] += temp_list[i-1]

    for i in range(N-1, -1, -1):
        sorted_list[temp_list[l[i]]-1] = l[i]
        temp_list[l[i]] -= 1

    return sorted_list   


"""--------------------------- Quicksort ---------------------------"""

def divide(l: list, first:int, last:int, pivot:int) ->int:
    """
    Divide l: all values smaller than the one indexed by the pivot at the left, the other at the right
    Args:
        l(list): list to sort
        first(int): first index of l in the initial list to sort
        last(int): last index of l in the initial list to sort
        pivot(int): pivot of the quicksort
    Returns:
        int: new pivot
    """

    l[pivot], l[last] = l[last], l[pivot]
    j = first
    for i in range(first, last):
        if l[i] <= l[last]:
            l[i], l[j] = l[j], l[i]
            j += 1
    l[j], l[last] = l[last], l[j]
    return j


def insertion_sort(l: list, first: int, last:int):
    """
    Args:
        l(list): list to sort
        first(int): first index of l in the initial list to sort
        last(int): last index of l in the initial list to sort
    """

    for i in range(first+1, last+1):
        val = l[i]
        j = i-1
        while j >= first and l[j] > val:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = val


def quicksort_v1(l: list, **kwargs):
    """
    Args:
        l(list): list to sort
        first(int): first index of l in the initial list to sort
        last(int): last index of l in the initial list to sort
    """

    first = kwargs.get('first', 0)
    last = kwargs.get('last', len(l)-1)

    if last - first >= 1:
        pivot = first
        pivot = divide(l, first, last, pivot)
        quicksort_v1(l, first=first, last=pivot-1)
        quicksort_v1(l, first=pivot+1, last=last)


def quicksort_v2(l: list, threshold=22, **kwargs):
    """
    Args:
        l(list): list to sort
        first(int): first index of l in the initial list to sort
        last(int): last index of l in the initial list to sort
        threshold(int): if the list's size is smaller than the threshold, insertion_sort is called
    """

    first = kwargs.get('first', 0)
    last = kwargs.get('last', len(l)-1)

    if last - first >= threshold:
        pivot = first
        pivot = divide(l, first, last, pivot)
        quicksort_v2(l, threshold=threshold, first=first, last=pivot-1)
        quicksort_v2(l, threshold=threshold, first=pivot+1, last=last)
    elif last - first >= 1:
        insertion_sort(l, first, last)


def quicksort_v3(l: list, threshold=34, **kwargs):
    """
    Args:
        l(list): list to sort
        first(int): first index of l in the initial list to sort
        last(int): last index of l in the initial list to sort
        threshold(int): if the list's size is smaller than the threshold, insertion_sort is called
    """

    first = kwargs.get('first', 0)
    last = kwargs.get('last', len(l)-1)

    if last - first >= threshold:
        pivot = randint(first, last)
        pivot = divide(l, first, last, pivot)
        quicksort_v3(l, threshold=threshold, first=first, last=pivot-1)
        quicksort_v3(l, threshold=threshold, first=pivot+1, last=last)
    elif last - first >= 1:
        insertion_sort(l, first, last)