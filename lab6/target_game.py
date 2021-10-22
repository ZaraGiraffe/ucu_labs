from typing import List
import itertools, random

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


def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
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
            if ch2:
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


print(get_user_words())


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    ch = get_words('lab6/en', letters)
    cout = []
    for i in user_words:
        if not i in ch:
            cout.append(i)
    return cout


def results():
    pass