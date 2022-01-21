from math import gcd


def reduceB(a, b):
    mod = 0
    for i in range(0, len(b)):
        mod = (mod * 10 + ord(b[i]) - 48) % a

    return mod


def gcdLarge(a, b):
    num = reduceB(a, b)
    return gcd(a, num)


for i in range(int(input())):
    a, b = int(input()), input()
    print(gcdLarge(a, b))
