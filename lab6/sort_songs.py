import doctest, math


def song_length(x):
    '''
    >>> song_length(('aboba', 3))
    3
    '''
    return x[1]


def title_length(x):
    '''
    >>> title_length(('aboba', 3))
    5
    '''
    return len(x[0])


def last_word(x):
    '''
    >>> last_word(('aboba aba', 3))
    'aba'
    '''
    return x[0].split()[-1].lower()


def sort_songs(song_titles, length_songs, key):
    '''
    sorts songs for a given key
    >>> sort_songs(['Янанебібув', 'Той день', 'Мало мені', 'Сосни', 'Кавачай', 'Відпусти', 'Африка', 'Поясни', 'Фіалки', 'Коли тебе нема', 'Етюд'], ['3.19', '3.58', '5.06', '4.31', '4.39', '3.52', '4.24', '3.39', '3.43', '3.17', '2.21'], title_length)
    [('Етюд', '2.21'), ('Сосни', '4.31'), ('Африка', '4.24'), ('Поясни', '3.39'), ('Фіалки', '3.43'), ('Кавачай', '4.39'), ('Той день', '3.58'), ('Відпусти', '3.52'), ('Мало мені', '5.06'), ('Янанебібув', '3.19'), ('Коли тебе нема', '3.17')]
    >>> sort_songs(['Янанебібув', 'Той день', 'Мало мені', 'Сосни', 'Кавачай', 'Відпусти', 'Африка', 'Поясни', 'Фіалки', 'Коли тебе нема', 'Етюд'], ['3.19', '3.58', '5.06', '4.31', '4.39', '3.52', '4.24', '3.39', '3.43', '3.17', '2.21'], song_length)
    [('Етюд', '2.21'), ('Коли тебе нема', '3.17'), ('Янанебібув', '3.19'), ('Поясни', '3.39'), ('Фіалки', '3.43'), ('Відпусти', '3.52'), ('Той день', '3.58'), ('Африка', '4.24'), ('Сосни', '4.31'), ('Кавачай', '4.39'), ('Мало мені', '5.06')]
    >>> sort_songs(['Янанебібув', 'Той день', 'Мало мені', 'Сосни', 'Кавачай', 'Відпусти', 'Африка', 'Поясни', 'Фіалки', 'Коли тебе нема', 'Етюд'], ['3.19', '3.58', '5.06', '4.31', '4.39', '3.52', '4.24', '3.39', '3.43', '3.17', '2.21'], last_word)
    [('Африка', '4.24'), ('Відпусти', '3.52'), ('Той день', '3.58'), ('Етюд', '2.21'), ('Кавачай', '4.39'), ('Мало мені', '5.06'), ('Коли тебе нема', '3.17'), ('Поясни', '3.39'), ('Сосни', '4.31'), ('Фіалки', '3.43'), ('Янанебібув', '3.19')]
    '''
    for i in song_titles:
        if not isinstance(i, str):
            return None
    for i in length_songs:
        if not isinstance(i, str):
            return None
    for i, v in enumerate(length_songs):
        if abs(math.floor(float(v)) - float(v)) <= 0.00001:
            length_songs[i] = int(v)
        else:
            length_songs[i] = float(v)
    if len(song_titles) != len(length_songs):
        return None
    rs = []
    for i in range(len(song_titles)):
        rs += [(song_titles[i], str(length_songs[i]))]
    rs.sort(key=key)
    return rs
