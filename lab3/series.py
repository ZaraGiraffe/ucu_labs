n = int(input())
print("1/2", end="")
for i in range(1, n):
    if i % 2:
        print(" - ", end="")
    else:
        print(" + ", end="")
    print(f"{i*2+1}/{i*2+2}", end="")
print()