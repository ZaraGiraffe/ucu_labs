import random


def generate_grid():
    """
    generates a grid
    """
    chars = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    lst1 = []
    while len(lst1) < 5:
        char = random.choice(chars)
        if not char in lst1:
            lst1 += [char]
    return lst1


def get_words(f, letters):
    '''
    gets words from file that starts from the letter that
    is int the list letters
    '''
    res = []
    with open(f, 'r') as file:
        for i in file:
            string = i.split()
            typ = ''
            add = [string[0], 'nothing']
            if len(string[0]) > 5 or string[0][0] not in letters:
                continue
            if string[1][0] == '/':
                typ = string[1][1:]
            else:
                typ = string[1]
            if typ[0] == 'a':
                if typ[2] == 'v':
                    add[1] = 'adverb'
                else:
                    add[1] = 'adjective'
            elif typ[0] == 'v':
                add[1] = 'verb'
            elif len(typ) == 1 and typ[0] == 'n':
                add[1] = 'noun'
            elif len(typ) > 1 and typ[0] == 'n' and typ[1] != 'o':
                add[1] = 'noun'
            elif len(typ) > 2 and typ[0] == 'n' and typ[2] == 'u':
                add[1] = 'noun'
            if add[1] != 'nothing':
                res += [tuple(add)]
    return res


def check_user_words(user_words, language_part, letters, dict_of_words):
    '''
    returns correct words and words that user missed
    '''
    if letters == None:
        return
    our = []
    for i in dict_of_words:
        if i[1] == language_part:
            our += [i[0]]
    res = []
    for i in user_words:
        if i in our:
            res += [i]
            our.remove(i)
    return res, our
