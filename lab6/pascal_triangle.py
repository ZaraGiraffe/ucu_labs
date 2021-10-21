import doctest


def generate_pascal_triangle(n):
    """
    creates pascal triangle
    >>> generate_pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    >>> generate_pascal_triangle(7)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1]]
    """
    if n <= 0:
        return []
    res = [[1]]
    for i in range(2, n+1):
        ins = [1]
        for j in range(i-1):
            if j == i-2:
                ins.append(1)
            else:
                ins.append(res[i-2][j] + res[i-2][j+1])
        res.append(ins)
    return res
