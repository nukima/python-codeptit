a = [0] * 95
a[1] = 1
a[2] = 1
for i in range(3,93):
    a[i] = a[i - 1] + a[i - 2]

t = int(input())
while (t > 0):
    t -= 1
    ab = input().split()
    A = int(ab[0])
    B = int(ab[1])

    for i in range (A, B + 1):
        print(a[i], end=" ")
    print()