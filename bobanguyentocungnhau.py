import math

n = [int(i) for i in input().split()]
l = n[0]
r = n[1]

for i in range(l, r - 1):
    for j in range(i + 1,  r):
        if math.gcd(i, j) == 1:
            for k in range(j + 1, r + 1):
                if (math.gcd(j, k) == 1) and (math.gcd(k, i) == 1):
                    print(f'({i}, {j}, {k})')