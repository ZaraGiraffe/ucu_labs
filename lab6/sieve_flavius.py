import doctest


def sieve_flavius(n):
    '''
    Returns list of lucky numbers
    >>> sieve_flavius(100)
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, 87, 93, 99]
    >>> sieve_flavius(10)
    [1, 3, 7, 9]
    >>> sieve_flavius(0)
    []
    '''
    mas = [i for i in range(1, n+1)]
    i1 = 1
    while i1 < len(mas):
        mas.remove(mas[i1])
        i1 += 1
    it = 1
    while(it < len(mas)):
        delete = mas[it]
        it2 = mas[it]-1
        while(it2 < len(mas)):
            mas.remove(mas[it2])
            it2 += delete-1
        it += 1
    return mas
