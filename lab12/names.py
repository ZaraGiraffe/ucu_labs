

def find_names(path):
    '''
    I am find_name
    >>> 'I am lol' == 'I am kek'
    False
    '''
    dct = {}
    with open(path, 'r') as file:
        num = int(file.readline())
        for i in range(num):
            str = file.readline()
            str = str.strip().split()
            name = str[0]
            num = int(str[1][1:-1])
            dct[name] = num
    res2 = [0, set()]
    for i in dct.keys():
        if dct[i] == 1:
            res2[0] += 1
            res2[1].add(i)
    res1 = set()
    for i, v in enumerate(sorted(list(dct.keys()), key = lambda x: -dct[x])):
        if i > 2:
            break
        res1.add(v)
    dct1 = {}
    for i, v in dct.items():
        if not i[0] in dct1.keys():
            dct1[i[0]] = [1, v]
        else:
            dct1[i[0]][0] += 1
            dct1[i[0]][1] += v
    k = sorted(list(dct1.keys()), key = lambda x: -dct1[x][0])[0]
    res3 = [k, dct1[k][0], dct1[k][1]]
    return tuple([res1, tuple(res2), tuple(res3)])
