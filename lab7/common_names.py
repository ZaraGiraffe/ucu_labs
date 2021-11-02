def common_names(female_names, male_names):
    '''
    returns common names
    >>> common_names([], [])
    set()
    '''
    lst = ['a', 'e', 'i', 'o', 'u', 'y']
    res = set()
    myset = set()
    for i in male_names:
        if i[0].lower() in lst:
            myset.add(i)
    for i in female_names:
        if i in myset and i[0].lower() in lst:
            res.add(i)
    return res


def names_read(file_name):
    """
    reads names from file
    """
    males = []
    with open(file_name, 'r') as file:
        for i in file:
            males.append(i.strip())
    return males
