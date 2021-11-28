def find_film_keywords(film_keywords: dict, film_name: str):
    '''
    I just want to solve problems from the site cses.fi
    >>> find_film_keywords({'1' : [1, 2, 3], '2' : [2, 3, 4]}, 1)
    {'1'}
    '''
    res = set()
    for i in film_keywords:
        if film_name in film_keywords[i]:
            res.add(i)
    return res


def find_films_with_keywords(film_keywords: dict, num_of_films: int):
    '''
    I don't want to code these labs...
    lets solve harded problems
    >>> find_films_with_keywords({'1' : [1, 2, 3], '2' : [3, 4, 5]}, 1)
    [(3, 2)]
    '''
    dct = {}
    for i in film_keywords:
        for j in film_keywords[i]:
            dct[j] = dct.get(j, 0) + 1
    res = list(dct.items())
    res.sort(key=lambda x: -x[1])
    return res[:num_of_films]
