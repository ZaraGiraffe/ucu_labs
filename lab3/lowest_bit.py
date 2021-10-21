a = int(input())
c = a & -a
sum = 0
while c != 1:
    sum += 1
    c /= 2
print(sum)