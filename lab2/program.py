import math


def sales_prediction():
    sum = float(input())
    res = sum * 1.19
    print(res)


def yard_to_meter():
    one_yard = 0.914
    yards = float(input())
    meters = yards * one_yard
    print(meters * 1000)
    print(meters)
    print(meters / 1000)



def cashier():
    pdv = 0.14
    tov = []
    sum = 0
    for i in range(5):
        tov.append(float(input()))
        sum += tov[i]
    print(int(sum))
    print(round(sum * pdv, 2))
    print(round(sum * (1 + pdv), 2))



def odometer():
    v = float(input())
    a = float(input())
    t1 = float(input())
    t2 = float(input())
    s1 = abs(v * t1 + a * t1**2 / 2)
    v = v + a * t1
    s2 = abs(v * t2)
    print(s1 + s2)

    


def payment_instalments():
    sum = float(input())
    kol = float(input())
    proc = 1.05
    print(sum * proc)
    print(sum * proc / kol)


def miles_per_galon():
    miles = float(input())
    gallons = float(input())
    print(miles / gallons)


def cookie():
    sug = 1.5
    but = 1
    bor = 2.75
    am = 48
    kol = float(input())
    print(sug * kol / am)
    print(but * kol / am)
    print(bor * kol / am)





def vineyard():
    r = float(input())
    e = float(input())
    s = float(input())
    print(int((r - 2 * e)/ s))


def compound_interest():
    p = float(input())
    r = float(input()) * 0.01
    n = int(input())
    t = int(input())
    a = p * (1 + r / n)**(n * t)
    print(a)



if __name__ == "__main__":
    eval(input() + "()")
