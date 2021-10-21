import math
x = float(input())
print("COS =", '{:.4f}'.format(math.cosh(x)))
print("EXP =", '{:.4f}'.format(0.5 * (math.exp(x) + math.exp(-x))))
print("E =", '{:.4f}'.format(0.5 * (math.e**x + math.e**-x)))
