from copy import deepcopy
from random import randint
import doctest

def linear_search(list, val):
    '''
    I am linear_search
    >>> linear_search([0, 1, 2], 2)
    2
    '''
    ind = -1
    for i, v in enumerate(list):
        if v == val:
            ind = i
            break
    return ind

def merge(seq1, seq2, seq):
    '''
    I am merge
    '''
    s1 = s2 = 0
    for i in range(len(seq)):
        if s1 >= len(seq1):
            seq[i] = seq2[s2]
            s2 += 1
        elif s2 >= len(seq2):
            seq[i] = seq1[s1]
            s1 += 1
        else:
            if seq1[s1] < seq2[s2]:
                seq[i] = seq1[s1]
                s1 += 1
            else:
                seq[i] = seq2[s2]
                s2 += 1

def merge_sort_dop(lst):
    '''
    I am merge_sort_dop
    '''
    if len(lst) > 1:
        mid = len(lst) // 2
        seq1, seq2 = lst[:mid], lst[mid:]
        merge_sort_dop(seq1)
        merge_sort_dop(seq2)
        merge(seq1, seq2, lst)

def merge_sort(lst):
    '''
    I am merge_sort
    >>> merge_sort([95, 69, 22, 83, 11, 78, 41, 57, 25, 33])
    [11, 22, 25, 33, 41, 57, 69, 78, 83, 95]
    '''
    lst1 = deepcopy(lst)
    merge_sort_dop(lst1)
    return lst1

def binary_search(lst, val):
    '''
    I am binary_search
    >>> binary_search([0, 1, 2, 3, 4, 5], 4)
    4
    '''
    l = 0
    r = len(lst)
    while r - l > 1:
        m = (l + r) // 2
        if lst[m-1] >= val:
            r = m
        else:
            l = m
    if lst[l] == val:
        return l
    else:
        return -1

def selection_sort(lst):
    '''
    I am selection_sort
    >>> selection_sort([5, 3, 6, 8, 1])
    [1, 3, 5, 6, 8]
    '''
    lst1 = deepcopy(lst)
    for bot in range(len(lst1)):
        for i in range(bot, len(lst1)):
            if lst1[i] < lst1[bot]:
                lst1[bot], lst1[i] = lst1[i], lst1[bot]
    return lst1

def quick_sort(lst):
    '''
    I am quick_sort
    >>> quick_sort([3, 4, 2, 6, 8])
    [2, 3, 4, 6, 8]
    '''
    if (len(lst) < 2):
        return lst
    ran = lst[randint(0, len(lst)-1)]
    less = []
    more = []
    equal = []
    for i, v in enumerate(lst):
        if v < ran:
            less.append(v)
        elif v > ran:
            more.append(v)
        else:
            equal.append(v)
    less = quick_sort(less)
    more = quick_sort(more)
    return less + equal + more
