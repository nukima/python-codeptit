# achilles
import math


def check(n):
    sum = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum += i
            if n % (i * i) != 0:
                return False
    if sum == n:
        return False
    return True


n = int(input())
if check(n):
    print(1)
else:
    print(0)
