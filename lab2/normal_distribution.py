import math
x = float(input())
u = float(input())
ro = float(input())
f = 1 / (2 * math.pi * ro**2)**0.5 *  math.exp(-1 * (x - u)**2 / (2 * ro**2))
print('{:.10f}'.format(f))
