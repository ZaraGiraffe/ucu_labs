
sum = 0
for i in range(5):
    k = int(input())
    if k > 100 or k < 0:
        print("None")
        exit()
    sum += k

sum /= 5
s = ""
if int(sum) >= 90:
    s = "A"
elif int(sum) >= 82:
    s = "B"
elif int(sum) >= 75:
    s = "C"
elif int(sum) >= 67:
    s = "D"
elif int(sum) >= 60:
    s = "E"
else:
    s = "F"
if int(sum) == 0:
    print(f"Average grade = {0} -> {s}")
else:
    print(f"Average grade = {sum} -> {s}")
