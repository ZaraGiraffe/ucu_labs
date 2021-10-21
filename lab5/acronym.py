def create_acronym(text: str):
    """
    creates an acronym
    >>> print(create_acronym("random access memory\\nAs soon As possible"))
    RAM - random access memory
    ASAP - As soon As possible
    """
    arr = text.split('\n')
    mas = ''
    for v, i in enumerate(arr):
        add = i.split()
        big = ''
        for j in add:
            big += j[0].upper()
        n = big + ' - ' + i
        mas += n
        if v != len(arr) - 1:
            mas += '\n'
    return mas
