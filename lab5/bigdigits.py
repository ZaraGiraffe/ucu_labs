import sys, doctest


Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]
Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]


def change():
    for i in range(len(Digits)):
        for j in range(len(Digits[i])):
            Digits[i][j] = Digits[i][j].replace("*", f"{i}")


change()


try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            line += digit[row]
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)


def return_digits(number):
    """
    returns number in a pretty way
    >>> return_digits('87654')
    ' 888 77777 666 55555   4  \\n8   8    76    5      44  \\n8   8   7 6    5     4 4  \\n 888   7  6666  555 4  4  \\n8   8 7   6   6    5444444\\n8   87    6   65   5   4  \\n 888 7     666  555    4  '
    >>> return_digits('456')
    '   4  55555 666 \\n  44  5    6    \\n 4 4  5    6    \\n4  4   555 6666 \\n444444    56   6\\n   4  5   56   6\\n   4   555  666 '
    """
    ans = ""
    arr = []
    for i in number:
        arr.append(int(i))
    arr.reverse()
    for j in range(len(One)):
        for i in range(len(arr)-1, -1, -1):
            ans += Digits[arr[i]][j]
        ans += '\n'
    return ans[:len(ans)-1]
