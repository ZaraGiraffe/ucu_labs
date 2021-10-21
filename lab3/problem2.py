a = int(input())
for i in range(1, a+1):
    s = ""
    for j in range(0, i):
        if j == 0 or j == i-1 or i == a:
            s += "*"
        else:
            s += " "
    print(s)


