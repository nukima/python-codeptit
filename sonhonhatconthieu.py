n = int(input())
b = [0] * 30001
a = input().split()
a = [int(i) for i in a]

for i in a:
    b[i] = 1
for i in range(1,30001):
    if b[i] == 0:
        print(i)
        break