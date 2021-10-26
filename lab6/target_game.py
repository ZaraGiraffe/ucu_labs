from typing import List
import random, copy

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    res1 = ''
    res = []
    for i in range(9):
        res1 += chr(ord('a') + random.randint(0, ord('z')-ord('a')))
    for i in range(3):
        res.append([])
        for j in range(3):
            res[i].append(res1[i*3 + j])
    return res


def get_words(f: str, grid: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    letters = copy.deepcopy(grid)
    res = []
    words = []
    have = letters[4]
    while letters:
        i = letters[0]
        cou = letters.count(i)
        while i in letters:
            letters.remove(i)
        for j in range(cou):
            words.append((i, j+1))
    with open(f, 'r') as file:
        for word in file:
            word = word.strip().lower()
            res1 = word
            if not have in word:
                continue
            ch = []
            while word:
                i = word[0]
                cou = word.count(i)
                word = word.replace(i, '')
                for j in range(cou):
                    ch.append((i, j+1))
            ch2 = True
            for i in ch:
                if not i in words:
                    ch2 = False
                    break
            if ch2 and len(res1) > 3:
                res.append(res1)
    return res


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    lst = []
    while True:
        try:
            lst.append(input())
        except EOFError:
            break
    return lst


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    cout = []
    for i in user_words:
        check = True
        if not letters[4] in i:
            check = False
        for j in i:
            if i.count(j) > letters.count(j):
                check = False
        if not i in words_from_dict and check:
            cout.append(i)
    return cout


def results():
    """
    prints result of the game
    """
    grid1 = generate_grid()
    grid = [grid1[i][j] for i in range(3) for j in range(3)]
    print(grid, grid1)
    words = get_words('./en', grid)
    user = get_user_words()
    pure = get_pure_user_words(user, grid, words)
    num = 0
    for i in user:
        if i in words:
            num += 1
            words.remove(i)
    res = words + pure
    with open('./result.txt', 'w') as file:
        file.write(str(num))
        file.write('\n')
        for i in res:
            file.write(i+'\n')
