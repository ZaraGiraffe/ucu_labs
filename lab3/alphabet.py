num = int(input())
mas = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
i = 1
j = 1
res = []
while num:
    s = ""
    for k in range(i, min(j, num)+i):
        s += " " + mas[k]
    res.append(s)
    num -= min(num, j)
    i += j
    j += 1
j -= 1
for i in range(j-1, -1, -1):
    res[j-1-i] = " " * i * 2 + res[j-1-i]

for i in range(j):
    print(res[i][1:])



    