import math


def Leibniz():
    n = 1
    for i in range(1, 8):
        n *= 10
        sum = 0
        for j in range(n):
            sum += (-1)**(j % 2) / (2*j + 1)
        print(f"elements in the series: {n}")
        print(f"difference: {abs(math.pi - 4 * sum)}")


def Archimede():
    d = 2
    count = 2
    for i in range(2, 15):
        count *= 2
        d = (2 - 2*(1 - d**2 / 4)**0.5)**0.5
        print(f"Number of sides: {count}")
        print(f"difference: {abs(math.pi - count * d / 2)}")


def Chudnovsky():
    for i in range(2, 10):
        sum = 0
        for j in range(i):
            sum += (-1)**(j % 2) * math.factorial(6*j) * (13591409 + 545140134*j) \
                / (math.factorial(3*j) * math.factorial(j)**3 * 640320**(3*j + 1.5))
        print(f"elements in the series: {i}")
        print(f"difference: {abs(math.pi - (sum*12)**-1)}")

            
def main():
    Leibniz()
    print()
    Archimede()
    print()
    Chudnovsky()


main()
