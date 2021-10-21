import math
st = int(input())
num = 5**st
num1 = num
sum = 0
while num > 0:
    r = num & 1
    sum += r
    num //= 2

if (sum % 2):
    print(f"Number {num1} is odious number. Its hamming weight is {sum}.")
else:
    print(f"Number {num1} is evil number. Its hamming weight is {sum}.")