t = int(input())
while t > 0:
    data = input().split()
    n = float(data[0])
    x = float(data[1]) / 100 + 1
    m = float(data[2])
    
    cnt = 0
    while n < m:
        n *= x
        cnt += 1
    print(cnt)
    t -= 1