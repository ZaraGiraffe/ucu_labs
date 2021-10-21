def get_number():
    """
    My variant
    """
    number = 98
    return number

# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None. They all include doctests, which you can
# test by running this file.

# The doctests are just examples. Feel free to add your own doctests.
# [2, 3, 5, 7, 11, 12, 13, 15, 19, 23, 25, 27] my tasks


# ****************************************
# Problem 2
# ****************************************
def compare_char(ch1, ch2):
    """
    (str, str) -> bool
    Compare two char by their position in alphabet. Register does not matter.
    Returns True if letter ch2 appears before ch1 and False otherwise. If
    neither ch1 nor ch2 are letters function returns None.

    >>> compare_char('a', 'z')
    False
    >>> compare_char('c', 'B')
    True
    >>> compare_char('d', 'ad')

    >>> compare_char('2xs', 2)

    """
    if not isinstance(ch1, str) or not isinstance(ch2, str):
        return None
    if len(ch1) > 1 or len(ch2) > 1:
        return None
    if len(ch1) == 0 or len(ch2) == 0:
        return None
    return ord(ch1.lower()) > ord(ch2.lower())


# ****************************************
# Problem 3
# ****************************************
def compare_str(s1, s2):
    """
    (str, str) -> bool
    Compare two srings lexicographicly. Register does not matter
    Return True if string s1 is larger than string s2 and False otherwise.
    If arguments aren't string or arguments have different length
    function returns None.

    >>> compare_str('abc', 'Abd')
    False
    >>> compare_str('zaD', 'zab')
    True
    >>> compare_str('zaD', 'Zad')
    False
    >>> compare_str('aaa', 'aaaaa')

    >>> compare_str('2015', 2015)

    """
    if not isinstance(s1, str) or not isinstance(s2, str):
        return None
    if len(s1) != len(s2):
        return None
    for i, v in enumerate(s1):
        if ord(v.lower()) > ord(s2[i].lower()):
            return True
        if ord(v.lower()) < ord(s2[i].lower()):
            return False
    return False


# ****************************************
# Problem 5
# ****************************************
def type_by_sides(a, b, c):
    """
    (float, float, float) -> str
    Detects the type of triangle by it's sides and returns type as string
    ("right angled triangle", "obutuse triangle", "acute triangle"). If there
    is no triangle with such sides, then function returns None.

    >>> type_by_sides(3, 3, 3)
    'acute triangle'
    >>> type_by_sides(3, 4, 5)
    'right angled triangle'
    >>> type_by_sides(3, 3, 2015)

    """
    masive = [a, b, c]
    new_masive = sorted(masive)
    if new_masive[0] + new_masive[1] <= new_masive[2]:
        return None
    elif new_masive[0]**2 + new_masive[1]**2 > new_masive[2]**2:
        return "acute triangle"
    elif new_masive[0]**2 + new_masive[1]**2 == new_masive[2]**2:
        return "right angled triangle"
    else:
        return "obutuse triangle"


# ****************************************
# Problem 7
# ****************************************
def convert_to_column(s):
    """
    str -> str
    Convert string to a column of words. Comas, dots, punctuation and
    question marks are omitted. If argument is not a string function returns
    None.

    >>> convert_to_column("Revenge is a dish that tastes \
        best when served cold.")
    'revenge
    is
    a
    dish
    that
    tastes
    best
    when
    served
    cold'
    >>> convert_to_column("Never hate your enemies. It affects your judgment.")
    'never
    hate
    your
    enemies
    it
    affects
    your
    judgment'
    >>> convert_to_column(2015)

    """
    if not isinstance(s, str):
        return None
    new_s = ""
    new_s = ""
    masive = s.split()
    lenght = len(masive)
    for i in range(lenght):
        if i != lenght-1:
            new_s += masive[i].strip("?").strip("!").strip(".")\
                .strip(",").lower() + "\n"
        else:
            new_s += masive[i].strip("?").strip("!")\
                .strip(".").strip(",").lower()
    return new_s


# ****************************************
# Problem 11
# ****************************************
def decrypt_message(s):
    """
    str -> str
    Replace all letters in string with previous letters in aplhabet.
    If argument isn't a string function returns None.

    >>> decrypt_message("Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpme.")
    'Revenge is a dish that tastes best when served cold.'
    >>> decrypt_message("Ofwfs ibuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou.")
    'Never hate your enemies. It affects your judgment.'
    >>> decrypt_message(2015)

    """
    if not isinstance(s, str):
        return None
    new_s = ""
    for i in s:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            new_s += chr(ord(i)-1)
        elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
            new_s += chr(ord(i)-1)
        else:
            new_s += i
    return new_s


# ****************************************
# Problem 12
# ****************************************
def exclude_letters(s1, s2):
    """
    (str, str) -> str
    Deletes all letter from string s2 in string s1.
    If arguments aren't strings function returns None.

    >>> exclude_letters("aaabb", "b")
    'aaa'
    >>> exclude_letters("abcc", "cczzyy")
    'ab'
    >>> exclude_letters(2015, "sasd")

    """
    if not isinstance(s1, str) or not isinstance(s2, str):
        return None

    def func(masive, exc):
        s = ""
        for i in masive:
            if i != exc:
                s += i
        return s
    for i in s2:
        s1 = func(s1, i)
    return s1


# ****************************************
# Problem 13
# ****************************************
def create_string(lst):
    """
    list -> str
    Creates and returns string from histogrma of letters. If argument isn't
    list of 26 positive integer numbers function returns None.

    >>> create_string([0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    'bcc'
    >>> create_string([4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4])
    'aaaazzzz'
    >>> create_string([4, 0, 0, 0, 0, 0])

    """
    if len(lst) != 26:
        return None
    s = ""
    for i, v in enumerate(lst):
        s += chr(ord('a')+i) * v
    return s


# ****************************************
# Problem 15
# ****************************************
def find_intersection(s1, s2):
    """
    (str, str) -> str
    Finds and returns string of all letters in alphabetic order that
    are present in both strings. If arguments aren't strings function
    should return None.

    >>> find_intersection("aaabb", "bbbbccc")
    'b'
    >>> find_intersection("aZAbc", "zzYYxp")
    'z'
    >>> find_intersection("sfdfsdf", 2015)

    """
    if not isinstance(s1, str) or not isinstance(s2, str):
        return None

    def func(s):
        masive = []
        for i in s:
            if i not in masive:
                masive.append(i)
        new_s = "".join(masive)
        return new_s
    s1 = func(s1.lower())
    s2 = func(s2.lower())
    new_s = ""
    for i in s1:
        if i in s2:
            new_s += i
    return new_s


# ****************************************
# Problem 19
# ****************************************
def polygon_area(vertices):
    """
    [(float, float), (float, float), (float, float), ...] -> float
    Takes coordinates of a convex polygon that are
    located clockwise and returns the area of this polygon

    >>> polygon_area([(4,10), (9,7), (11,2), (2,2)])
    45.5
    >>> polygon_area([(9,7), (11,2), (2,2), (4, 10)])
    45.5
    >>> polygon_area([(0, 0), (0.5,1), (1,0)])
    0.5
    >>> polygon_area([(0, 10), (0.5,11), (1,10)])
    0.5
    >>> polygon_area([(-0.5, 10), (0,-11), (0.5,10)])
    10.5
    """
    s = 0
    for i, v in enumerate(vertices):
        fir = v
        sec = vertices[(i+1) % len(vertices)]
        s += fir[0]*sec[1] - fir[1]*sec[0]
    return abs(s)/2


# ****************************************
# Problem 23
# ****************************************
def one_swap_sorting(sequence):
    """
    [int, int, int, ...] -> bool
    Takes a list of integers and returns whether it can be sorted
    via one swap of any two integer in the list. The swap is obligatory

    >>> one_swap_sorting([0,1,2,3])
    False
    >>> one_swap_sorting([])
    False
    >>> one_swap_sorting([42])
    False
    >>> one_swap_sorting([3,2])
    True
    >>> one_swap_sorting([2,2])
    True
    >>> one_swap_sorting([5,2,3,4,1,6])
    True
    >>> one_swap_sorting([1,2,3,5,4])
    True
    """
    if len(sequence) < 2:
        return False
    masive = sorted(sequence)
    check = 0
    for i, v in enumerate(masive):
        if v != sequence[i]:
            check += 1
    equal = False
    for i in range(1, len(masive)):
        if masive[i] == masive[i-1]:
            equal = True
            break
    if check == 2 or (check == 0 and equal):
        return True
    else:
        return False


# ****************************************
# Problem 25
# ****************************************
def happy_number(n):
    """
    int -> bool
    Takes an integer and checks whether iy is happy. Integer is called happy
    if a sequence that starts with the integer and every next integer
    is the sum of squares of digits of the previous integer in the sequence.

    >>> happy_number(32)
    True
    >>> happy_number(33)
    False
    """
    if n == 1:
        return True
    masive = [n]

    def func(n):
        s = 0
        while n != 0:
            s += (n % 10)**2
            n //= 10
        return s
    while func(masive[-1]) not in masive:
        if func(masive[-1]) == 1:
            return True
        masive.append(func(masive[-1]))
    return False


# ****************************************
# Problem 27
# ****************************************
def turn_over(n, lst):
    """
    Reverse first n items of the list and return it.
    If n < 0 that it reverses the last n items of the list.
    if absolute value of n is more than the lenght of the list
    returns None

    >>> turn_over(4, ['f', 'o', 'o', 't', 'b', 'a', 'l', 'l'])
    ['t', 'o', 'o', 'f', 'b', 'a', 'l', 'l']
    >>> turn_over(-5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]
    >>> turn_over(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> turn_over(-5, [])

    """
    if abs(n) > len(lst):
        return None
    neg = n < 0
    n = abs(n)
    if neg:
        lst.reverse()
    new = []
    for i in range(n):
        new.append(lst[i])
    new.reverse()
    for i in range(n):
        lst[i] = new[i]
    if neg:
        lst.reverse()
    return lst


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
