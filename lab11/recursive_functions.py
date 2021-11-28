def create_table(n, m):
    '''
    bla bla
    >>> create_table(4, 6)
    [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21], [1, 4, 10, 20, 35, 56]]
    '''
    mas = [[1 for i in range(m)] for j in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            mas[i][j] = mas[i-1][j] + mas[i][j-1]
    return mas

def flatten(lst):
    '''
    bla bla
    >>> flatten([1,2,[3,[4,5],6],7])
    [1, 2, 3, 4, 5, 6, 7]
    '''
    if not isinstance(lst, list):
        return lst
    elif len(lst) == 1:
        return flatten(lst[0])
    elif len(lst) == 0:
        return []
    else:
        fir = flatten(lst[0])
        sec = flatten(lst[1:])
        if not isinstance(fir, list):
            fir = [fir]
        if not isinstance(sec, list):
            sec = [sec]
        return fir + sec
