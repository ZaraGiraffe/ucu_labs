# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None.
def find_max_1(fun, points):
    """
    (function or str, list(number)) -> (number)

    Find and return maximal value of function f in points.

    >>> find_max_1('x ** 2 + x', [1, 2, 3, -1])
    12
    >>> find_max_1(lambda x: x ** 2 + x, [1, 2, 3, -1])
    12
    """
    if isinstance(fun, str):
        return max(map(lambda x : eval(fun), points))
    else:
        return max(map(fun, points))

def find_max_2(fun, points):
    """
    (function or str, list(number)) -> (number)

    Find and return list of points where function f has the maximal value.

    >>> find_max_2('x ** 2 + x', [1, 2, 3, -1])
    [3]
    >>> find_max_2(lambda x: x ** 2 + x, [1, 2, 3, -1])
    [3]
    """
    ma = max(map(lambda x : eval(fun), points)) if isinstance(fun, str) \
        else max(map(fun, points))
    newp = map(lambda x : eval(fun), points) if isinstance(fun, str) \
        else map(fun, points)
    res = []
    for i, v in enumerate(newp):
        if v == ma:
            res.append(points[i])
    return res


def compute_limit(seq):
    """
    (function or str) -> (number)

    Compute and return limit of a convergent sequence.

    >>> compute_limit('(n ** 2 + n) / n ** 2')
    1.0
    >>> compute_limit(lambda n: (n ** 2 + n) / n ** 2)
    1.0
    """
    eee = 0.00001
    nun = 10
    fun = (lambda n: eval(seq)) if isinstance(seq, str) else seq
    while abs(fun(nun) - fun(nun-1)) > eee:
        nun *= 10
        if nun > 10**20:
            break
    return round(fun(nun), 2)

def compute_derivative(fun, x_0):
    """
    (function or str, number) -> (number)

    Compute and return derivative of function f in the point x_0.

    >>> compute_derivative('x ** 2 + x', 2)
    5.0
    >>> compute_derivative(lambda x: x ** 2 + x, 2)
    5.0
    """
    eee = 0.00001
    nun = 10
    x_1 = x_0 + nun
    fn1 = (lambda x: eval(fun)) if isinstance(fun, str) else fun
    dod = [0, 1]
    while abs(dod[-1] - dod[-2]) > eee:
        nun /= 10
        x_1 = x_0 + nun
        kuq = (fn1(x_1) - fn1(x_0)) / nun
        dod.append(kuq)
        if nun < 10**(-10):
            break
    return round(dod[-1], 2)

def get_tangent(fun, x_0):
    """
    (function or str, number) -> (str)

    Compute and return tangent line to function f in the point x_0.

    >>> get_tangent('x ** 2 + x', 2)
    '5.0 * x - 4.0'
    >>> get_tangent('- x ** 2 + x', 2)
    '- 3.0 * x + 4.0'
    >>> get_tangent(lambda x: x ** 2 + x, 2)
    '5.0 * x - 4.0'
    >>> get_tangent(lambda x: - x ** 2 + x, 2)
    '- 3.0 * x + 4.0'
    """
    fn1 = (lambda x : eval(fun)) if isinstance(fun, str) else fun
    der = compute_derivative(fun, x_0)
    kal = fn1(x_0)
    lul = -x_0 * der
    bab = kal + lul
    eee = 0.0001
    return f'{"- " if der < 0 else ""}{abs(der)} * x {"-" if bab < 0 else "+"} {abs(round(bab, 2))}'

def get_root(fun, a_0, b_0):
    """
    (function or str, number, number) -> (number)

    Compute and return root of the function f in the interval (a, b).

    >>> get_root('x', -1, 1)
    0.0
    >>> get_root(lambda x: x, -1, 1)
    0.0
    """
    fn1 = (lambda x: eval(fun)) if isinstance(fun, str) else fun
    eee = 0.00001
    count = 0
    while abs(fn1(a_0 + b_0 / 2)) > eee:
        mom = (a_0 + b_0) / 2
        if fn1(a_0) * fn1(mom) > 0:
            a_0 = mom
        else:
            b_0 = mom
        count += 1
        if count > 20:
            break
    mom = (a_0 + b_0) / 2
    if abs(mom) < eee:
        return abs(round(mom, 2))
    else:
        return round(mom, 2)
