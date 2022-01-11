t = int(input())
while (t > 0):
    n = input()
    if n[0:2] == n[-2:]:
        print("YES")
    else:
        print("NO")
    t -= 1