import doctest


def happy_number(number: int) -> bool:
    mas = []
    for i in range(8):
        mas.append(number % 10)
        number //= 10
    suml, sumr = 0, 0
    for i in range(8):
        if i < 4:
            suml += mas[i]
        else:
            sumr += mas[i]
    if suml == sumr:
        return True
    else:
        return False


def count_happy_numbers(n: int) -> bool:
    '''
    returns the number of happy numbers from 1 to n
    >>> count_happy_numbers(100)
    1
    >>> count_happy_numbers(378764)
    4030
    '''
    res = 0
    for i in range(n+1):
        if happy_number(i):
            res += 1
    return res


def happy_numbers(m: int, n: int) -> list:
    '''
    returns the number of happy numbers from m to n
    >>> happy_numbers(5, 78)
    0
    >>> happy_numbers(234255, 451251)
    3503
    '''
    res = 0
    for i in range(m, n+1):
        if happy_number(i):
            res += 1
    return res
