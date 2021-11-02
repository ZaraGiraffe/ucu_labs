def dict_reader_tuple(file_dict):
    '''
    returns list
    '''
    res = []
    with open(file_dict, 'r') as file:
        for i in file:
            lst = i.strip().split()
            res.append(tuple([lst[0], int(lst[1]), lst[2:]]))
    return res


def dict_reader_dict(file_dict):
    '''
    returns dict
    '''
    res = {}
    with open(file_dict, 'r') as file:
        for i in file:
            lst = i.strip().split()
            if lst[0] not in res:
                res[lst[0]] = set()
            res[lst[0]].add(tuple(lst[2:]))
    return res


def dict_sort(dict: dict):
    '''
    sorts dict by keys
    '''
    res = {}
    s = sorted(dict.keys())
    for i in s:
        res[i] = dict[i]
    return res


def dict_invert1(dct: list):
    '''
    dict_invert for list
    '''
    res = {}
    lst_count = {}
    for i in dct:
        lst_count[i[0]] = lst_count.get(i[0], 0) + 1
    for i in dct:
        if lst_count[i[0]] not in res:
            res[lst_count[i[0]]] = set()
        s = tuple([i[0], tuple(i[2])])
        res[lst_count[i[0]]].add(s)
    return dict_sort(res)


def dict_invert2(dct: dict):
    '''
    dict_invert for dict
    '''
    res = {}
    for i in dct:
        if len(dct[i]) not in res:
            res[len(dct[i])] = set()
        for j in dct[i]:
            res[len(dct[i])].add((i, j))
    return dict_sort(res)


def dict_invert(dct):
    '''
    returns inverted dict/list
    >>> dict_invert({'WATER':{('W','A','T','E','R')}})
    {1: {('WATER', ('W', 'A', 'T', 'E', 'R'))}}
    '''
    if isinstance(dct, list):
        return dict_invert1(dct)
    else:
        return dict_invert2(dct)
