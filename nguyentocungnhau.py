import math

n_k = input().split()
n = int(n_k[0])
k = int(n_k[1])

count = 1
for i in range(10**(k - 1), 10**k):
    if math.gcd(n, i) == 1:
        if count == 10:
            print(i)
            count = 1
        else:
            print(i, end=' ')
            count += 1