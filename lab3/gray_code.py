a = input()
b = ""
for i in range(len(a)-1, 0, -1):
    print(i, a[i], str(int(a[i]) ^ int(a[i-1])))
    b += str(int(a[i]) ^ int(a[i-1]))
b += a[0]
print(b[::-1])
