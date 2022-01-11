t = int(input())
while t > 0:
    t -= 1
    s = input()
    sum = 0
    for i in s:
        sum += ord(i) - ord('0')
    if sum % 3 == 0:
        print("YES")
    else:
        print("NO")