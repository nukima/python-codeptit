def check(n):
    for i in range(len(n) - 1):
        if n[i] > n[i+1]:
            return False
    return True

t = int(input())
for i in range(t):
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")
