def check(n):
    oo = ord('0')
    sum = ord(n[0]) - oo
    for i in range(1,len(n)):
        if abs(ord(n[i]) - ord(n[i - 1])) != 2:
            return False
        sum += ord(n[i]) - oo
    if sum % 10 == 0:
        return True
    else:
        return False

t = int(input())
while (t > 0):
    t -= 1
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")