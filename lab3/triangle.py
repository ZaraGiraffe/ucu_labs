st = int(input())
num = int(input())
for bla in range(num, 0, -1):
    print(st, end="")
    for i in range(st+1, st+bla):
        print(end=" ")
        print(i, end="")
    print()
