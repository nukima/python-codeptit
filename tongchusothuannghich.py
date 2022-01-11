def check(n):
    l = len(n)
    if l == 1: return False
    for i in range(l//2):
        if n[i] != n[l - 1 - i]:
            return False
    return True


t = int(input())
while t > 0:
    t -= 1
    s = input()
    sum = 0
    for i in s:
        sum += ord(i) - ord('0')
    if check(str(sum)):
        print("YES")
    else:
        print("NO")