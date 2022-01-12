def Try(n, k):
    if n == 1:
        return "A"
    mid_idx = (2 ** n - 1) // 2
    if k == mid_idx:
        return chr(65 + n - 1)
    elif k < mid_idx:
        return Try(n - 1, k)
    else:
        return Try(n - 1, k - mid_idx - 1)


t = int(input())
for i in range(t):
    n, k = [int(_) for _ in input().split()]
    k -= 1
    print(Try(n, k))
