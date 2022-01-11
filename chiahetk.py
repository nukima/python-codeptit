akn = input().split()
a = int(akn[0])
k = int(akn[1])
n = int(akn[2])

b = k - abs(a % k)
cnt = 0
while (b <= n - a):
    if (a + b) % k == 0:
        print(b, end=" ")
        cnt += 1
    b += k

if cnt == 0:
    print(-1)