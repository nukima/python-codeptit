import math

t = int(input())
while t > 0:
    n = int(input())
    t -= 1

    print("1", end=" ")
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                n /= i
                cnt += 1
            print("* " + f"{i}" + "^" + f"{cnt}", end=" ")
    if n != 1:
        n = int(n)
        print(f"* {n}^1")
    else:
        print()
