from math import sqrt

n = int(input())
result = 1
for _ in range(n):
    sum = 0
    n = int(input())
    while n % 2 == 0:
        sum += 2
        n /= 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            sum += i
            n /= i

    if n > 2:
        sum += n

    result *= sum

print(int(result))
