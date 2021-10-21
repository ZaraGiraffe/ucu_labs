epsilon = 0.000000001


def lines_intersection(k1, c1, k2, c2):
    if abs(k1 - k2) < epsilon:
        return None
    x = (c2 - c1) / (k1 - k2)
    y = x * k1 + c1
    return x, y


def distance(x1, y1, x2, y2):
    return (abs(x1-x2)**2 + abs(y1 - y2)**2)**0.5


def quadrangle_area(a, b, c, d, f1, f2):
    return (4 * f1**2 * f2**2 - (b**2 + d**2 - a**2 - c**2)**2)**0.5 / 4


def four_lines_area(k1, c1, k2, c2, k3, c3, k4, c4):
    if k3 != k1:
        print("k1 has to be equal k3")
    if lines_intersection(k1, c1, k2, c2) == None or lines_intersection(k1, c1, k4, c4) == None:
        return None
    x1, y1 = lines_intersection(k1, c1, k2, c2)
    x2, y2 = lines_intersection(k2, c2, k3, c3)
    x3, y3 = lines_intersection(k3, c3, k4, c4)
    x4, y4 = lines_intersection(k4, c4, k1, c1)
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x4, y4)
    d = distance(x4, y4, x1, y1)
    f1 = distance(x1, y1, x3, y3)
    f2 = distance(x2, y2, x4, y4)
    return quadrangle_area(a, b, c, d, f1, f2)


