a, b = [int(x) for x in input().split()]
sum = 0
while (a != 0 or b != 0):
    sum += (a % 2) ^ (b % 2)
    a >>= 1
    b >>= 1
print(sum)