t = int(input())
while t > 0:
    text = input()
    char = [c for c in text if c >= 'A' and c <= 'Z']
    char.sort()
    num = [int(c) for c in text if c >= '0' and c <= '9']
    print(*char, sum(num), sep='')
    t -= 1
