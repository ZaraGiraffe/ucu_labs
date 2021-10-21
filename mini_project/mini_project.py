from random import randint
from copy import copy


def cin(first = 0):
    while True:
        try:
            y = input()
            if (y == "stop"):
                return None
            y = int(y)
            if ((y <= 0 or y > 10) and first):
                raise ZeroDivisionError
            return y
        except:
            print("this number is not in the right format")
            print("try again: ")
            print(">>> ", end="")


def cindop(num_len):
    print("enter the number: ")
    print(">>> ", end="")
    chel_num = cin()
    if (chel_num == None):
        return None
    while chel_num >= 10 ** num_len or chel_num < 10 ** (num_len - 1):
        print("this number is not in the right format")
        print("try again: ")
        print(">>> ", end="")
        chel_num = cin()
        if (chel_num == None):
            return None
    return chel_num


def game():
    print("len of the number: ")
    print(">>> ", end="")
    num_len = cin(first = 1)
    if (num_len == None):
        print("waiting for your next game")
        return
    num = 0
    count = 0
    num += randint(1, 9) * 10 ** (num_len - 1)
    if (num_len != 1):
        num += randint(1, 10 ** (num_len - 1) - 1)
    num1 = num
    mas_num = []
    while num != 0:
        mas_num.append(num % 10)
        num //= 10

    while True:
        chel_num = cindop(num_len)
        if (chel_num == num1):
            print(f"yes! thу number is {num1}")
            print(f"you used {count+1} questions")
            break
        if (chel_num == None):
            print(f"you are loser!!!")
            print(f"the number was {num1}")
            break

        mas_chel_num = []
        while chel_num != 0:
            mas_chel_num.append(chel_num % 10)
            chel_num //= 10

        mas_num_dop = copy(mas_num)
        bulls = 0
        cows = 0
        for i in range(num_len):
            if mas_num_dop[i] == mas_chel_num[i]:
                bulls += 1
                mas_num_dop[i] = -1
                mas_chel_num[i] = -1
        for i in range(10):
            first = mas_num_dop.count(i)
            second = mas_chel_num.count(i)
            cows += min(first, second)
        print(f"cows = {cows}, bulls = {bulls}")
        count += 1


game()
