def calc(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + calc(n/2)
    else:
        return 1 + calc(n*3 + 1)

while True:
    t = int(input())
    if t == 0: break
    cnt = 1
    print(calc(t))