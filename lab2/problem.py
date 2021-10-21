import math
r = float(input())
h = float(input())
V = round(h * r**2 * math.pi, 3)
A = round(2 * h * math.pi * r + 2 * math.pi * r**2, 3)

print("V = ", V)
print("A = ", A)
