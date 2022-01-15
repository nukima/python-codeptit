n = int(input())
a = [int(_) for _ in input().split()]
count = 0
tmp_1, tmp_2 = 0, 0
for i in range(0, n - 1, 1):
    if a[i] * a[i + 1] > 0:
        count += 1
        tmp_1, tmp_2 = a[i], a[i + 1]
        
if count > 0:
    print(count, tmp_1, tmp_2, sep=' ')
else:
    print('0')