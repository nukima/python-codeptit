t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = [0] * n
    b = [0] * 1001

    for i in range (n):
        a[i] =  int(input())
        b[a[i]] += 1

    cnt = b[a[0]]
    k = a[0]
    for i in range(1,n):
        if  cnt < b[a[i]]:
            cnt = b[a[i]]
            k = a[i]
        if  cnt == b[a[i]] and k > a[i]:
            cnt = b[a[i]]
            k = a[i]
    print(k)