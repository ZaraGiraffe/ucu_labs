'''
This program returns oriented area of oriented quadraliteral
(the area will be positive if vertices go in counter clocwise order)
'''
epsilon = 0.000000001


def area(x1, y1, x2, y2):
    return x1 * y2 - x2 * y1


def lines_intersection(k1, c1, k2, c2):
    if abs(k1 - k2) < epsilon:
        return None
    x = (c2 - c1) / (k1 - k2)
    y = x * k1 + c1
    return x, y


def area_quadraliteral(x1, y1, x2, y2, x3, y3, x4, y4):
    area_sum = 0
    area_sum += area(x1, y1, x2, y2) / 2
    area_sum += area(x2, y2, x3, y3) / 2
    area_sum += area(x3, y3, x4, y4) / 2
    area_sum += area(x4, y4, x1, y1) / 2
    return area_sum


def four_lines_area(k1, c1, k2, c2, k3, c3, k4, c4):
    pass






