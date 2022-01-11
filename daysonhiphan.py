n = int(input())
a = input().split()
a = [int(i) for i in a]
cnt = 0
for i in range(n - 1):
    if a[i] != a[i + 1]:
        cnt += 1
print(cnt)