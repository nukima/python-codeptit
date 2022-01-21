def run(n):
    if n % 7 == 0:
        return n
    for i in range(1000):
        n += int(str(n)[::-1])
        if n % 7 == 0:
            return n

    return -1


for _ in range(int(input())):
    n = int(input())
    print(run(n))
