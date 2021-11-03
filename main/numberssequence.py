def test(form):
    '''
    checks whether form has even numbers of bits
    excluding the first bit
    >>> test(8)
    False
    '''
    form //= 2
    mas = []
    while form > 0:
        mas.append(form % 2)
        form //= 2
    if mas.count(1) == 0 or mas.count(1) % 2:
        return False
    return True


def pyramidal_numbers(length):
    """
    returns length pyramidal numbers
    >>> pyramidal_numbers(3)
    [12, 792, 1125]
    """
    res = []
    i = 1
    while len(res) < length:
        form = i * (i + 1) * (3 * i - 2) // 2
        if test(form):
            res.append(form)
        i += 1
    return res
