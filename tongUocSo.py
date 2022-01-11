from math import sqrt

t = int(input())
sum = 0
for i in range(t):
    n = int(input())
    while n % 2 == 0:
        sum += 2
        n /= 2
    for j in range(3, int(sqrt(n)) + 1, 2):
        while n % j == 0:
            sum += j
            n /= j
    if n > 2:
        sum += n
print(int(sum))
