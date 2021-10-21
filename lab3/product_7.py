a = int(input())
dob = 1
for i in range(1, a+1):
    if i % 7:
        dob *= i
print(dob)