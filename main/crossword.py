def read_crossword(path):
    '''
    reads symbols from file
    '''
    res = []
    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            fir = line[0]
            line = line[1:]
            while len(line) > 0:
                dop = (fir, (int(line[0]), int(line[1])))
                res.append(dop)
                line = line[2:]
    return res


def crossword_words(crossword):
    """
    returns the longest words in crossword
    >>> crossword_words([('e', (4, 6)), ('v', (5, 6)), ('t', (6, 6)), ('t', (3, 2)), ('r', (4, 7))])
    ['evt']
    """
    mas = [['0' for i in range(10)] for j in range(10)]
    for i in crossword:
        x = i[1][0]
        y = i[1][1]
        mas[x][y] = i[0]
    maxl = 3
    res = []
    for y in range(10):
        s = ""
        for x in range(10):
            if mas[x][y] == '0':
                s += " "
            else:
                s += mas[x][y]
        words = s.split()
        for i in words:
            if len(i) == maxl:
                res.append(i)
            if len(i) > maxl:
                res.clear()
                res.append(i)
                maxl = len(i)
    return res
