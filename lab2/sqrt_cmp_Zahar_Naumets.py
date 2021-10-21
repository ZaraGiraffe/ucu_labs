import math

epsilon = 0.01


def exhaustive_enumeration(x):
    step = epsilon**2
    numGuesses = 0
    ans = 0.0
    while abs(ans**2 - x) >= epsilon and ans <= x:
        ans += step
        numGuesses += 1
    if abs(ans**2 - x) >= epsilon:
        print("Failed")
    else:
        print(f"Guesses: {numGuesses:10}, answer: {ans:.15f}, difference: {abs(ans - math.sqrt(x)):.15f}")


def bissection_search(x):
    numGuesses = 0
    low = 0
    high = max(1.0, x)
    ans = (high + low) / 2.0
    while abs(ans**2 - x) >= epsilon:
        numGuesses += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    print(f"Guesses: {numGuesses:10}, answer: {ans:.15f}, difference: {abs(ans - math.sqrt(x)):.15f}")


def Newton_Raphson(x):
    numGuesses = 0
    ans = x / 2
    while ans**2 - x >= epsilon:
        numGuesses += 1
        ans = ans - ((ans**2 - x) / (2 * ans))
    print(f"Guesses: {numGuesses:10}, answer: {ans:.15f}, difference: {abs(ans - math.sqrt(x)):.15f}")


def main():
    x = float(input("Enter x: "))
    print("Exhaustive enumeration: ")
    exhaustive_enumeration(x)
    print("Bissection search: ")
    bissection_search(x)
    print("Newton-Raphson: ")
    Newton_Raphson(x)


main()

     