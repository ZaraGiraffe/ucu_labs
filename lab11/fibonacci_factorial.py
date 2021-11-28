import time, doctest

def factorial_recursive(n):
    '''
    bla bla
    >>> factorial_recursive(3)
    6
    '''
    if n == 0:
        return 1
    else:
        return factorial_recursive(n-1) * n

def factorial_iterative(n):
    '''
    bla bla
    >>> factorial_iterative(3)
    6
    '''
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def fibonacci_recursive(n):
    '''
    bla bla
    >>> fibonacci_recursive(3)
    3
    '''
    if n == 1 or n == 0:
        return 1
    else:
        return fibonacci_recursive(n-2) + fibonacci_recursive(n-1)

def fibonacci_iterative(n):
    '''
    bla bla
    >>> fibonacci_recursive(3)
    3
    '''
    if n == 1 or n == 0:
        return 1
    else:
        mas = [1 for i in range(n+1)]
        for i in range(2, n+1):
            mas[i] = mas[i-1] + mas[i-2]
        return mas[n]

def numbers_time_test(function=0, realisation=0, verbose=False):
    '''
    bla bla
    '''
    num = 20 if verbose else 5
    fuc = factorial_recursive
    string = 'factorial_recursive'
    if function == 0 and realisation == 1:
        fuc = factorial_iterative
        string = 'factorial_iterative'
    elif function == 1 and realisation == 0:
        fuc = fibonacci_recursive
        string = 'fibonacci_recursive'
    elif function == 1 and realisation == 1:
        fuc = fibonacci_iterative
        string = 'fibonacci_iterative'
    for i in range(1, num+1):
        st = time.time()
        res = fuc(i)
        end = time.time() - st
        print(string + f'({i}) works {end} seconds and returns {res}')
numbers_time_test()