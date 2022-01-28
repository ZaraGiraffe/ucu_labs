#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    This is an example of a bot for the 3rd project.
    ...a pretty bad bot to be honest -_-
"""

from logging import DEBUG, debug, getLogger
from random import choice

# We use the debugger to print messages to stderr
# You cannot use print as you usually do, the vm would intercept it
# You can hovever do the following:
#
# import sys
# print("HEHEY", file=sys.stderr)

getLogger().setLevel(DEBUG)


def parse_field_info():
    """
    Parse the info about the field.

    However, the function doesn't do anything with it. Since the height of the field is
    hard-coded later, this bot won't work with maps of different height.

    The input may look like this:

    Plateau 15 17:
    """
    l = input()
    l = l.strip().split()
    row, col = int(l[1]), int(l[2][:-1])
    return row, col


def parse_field(row):
    """
    Parse the field.

    First of all, this function is also responsible for determining the next
    move. Actually, this function should rather only parse the field, and return
    it to another function, where the logic for choosing the move will be.

    Also, the algorithm for choosing the right move is wrong. This function
    finds the first position of _our_ character, and outputs it. However, it
    doesn't guarantee that the figure will be connected to only one cell of our
    territory. It can not be connected at all (for example, when the figure has
    empty cells), or it can be connected with multiple cells of our territory.
    That's definitely what you should address.

    Also, it might be useful to distinguish between lowecase (the most recent piece)
    and uppercase letters to determine where the enemy is moving etc.

    The input may look like this:

    01234567890123456
    000 .................
    001 .................
    002 .................
    003 .................
    004 .................
    005 .................
    006 .................
    007 ..O..............
    008 ..OOO............
    009 .................
    010 .................
    011 .................
    012 ..............X..
    013 .................
    014 .................

    :param player int: Represents whether we're the first or second player
    """
    l = input().strip()
    mas = []
    for i in range(row):
        mas.append(input().strip().split()[1])
    return mas


def parse_figure():
    """
    Parse the figure.

    The function parses the height of the figure (maybe the width would be
    useful as well), and then reads it.
    It would be nice to save it and return for further usage.

    The input may look like this:

    Piece 2 2:
    **
    ..
    """
    l = input()
    row = int(l.strip().split()[1])
    mas = []
    for i in range(row):
        mas.append(input().strip())
    return mas


def step(player: int):
    """
    Perform one step of the game.

    :param player int: Represents whether we're the first or second player
    """
    char = 'O'
    notchar = 'X'
    if player == 2:
        char = 'X'
        notchar = 'O'
    row, col = parse_field_info()
    field = parse_field(row)
    fig = parse_figure()
    frow, fcol = len(fig), len(fig[0])
    steps = []
    for i in range(row):
        for j in range(col):
            check = 1
            spiv = 0
            for i1 in range(frow):
                for j1 in range(fcol):
                    i2 = i + i1
                    j2 = j + j1
                    if i2 < 0 or i2 >= row or j2 < 0 or j2 >= col:
                        check = 0
                        continue
                    if fig[i1][j1] == '.':
                        continue
                    if field[i2][j2] == notchar:
                        check = 0
                        continue
                    if field[i2][j2] == char:
                        spiv += 1
            if check == 1 and spiv == 1:
                steps.append((i, j))
    if len(steps) == 0:
        return (0, 0)
    else:
        mrow = int(row / 2)
        mcol = int(col / 2)
        steps.sort(key=lambda x: abs(x[0] - mrow) + abs(x[1] - mcol))
        return steps[0]


def play(player: int):
    """
    Main game loop.

    :param player int: Represents whether we're the first or second player
    """
    while True:
        move = step(player)
        print(*move)

def parse_info_about_player():
    """
    This function parses the info about the player

    It can look like this:

    $$$ exec p2 : [./player1.py]
    """
    i = input()
    debug(f"Info about the player: {i}")
    return 1 if "p1 :" in i else 2


def main():

    player = parse_info_about_player()
    try:
        play(player)
    except EOFError:
        debug("Cannot get input. Seems that we've lost ):")


if __name__ == "__main__":
    main()
