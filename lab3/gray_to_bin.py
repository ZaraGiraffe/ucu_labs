grey = input()
res = grey[0]
for i in range(1, len(grey)):
    res += str(int(grey[i]) ^ int(res[i-1]))
print(res)