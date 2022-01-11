nx = input().split()
n = int(nx[0])
x = int(nx[1])
prime = [True for i in range(10000)]
dis = [0] * n
dis[0] = 2
p = 3
index = 1

while (index < n):    
    if (prime[p] == True):
        dis[index] = p
        index += 1
        for i in range(p ** 2, 10000, p):
            prime[i] = False
    p += 2

print(x, end=" ")
tmp = x
for i in range (n):
    tmp = tmp + dis[i]
    print(tmp, end=" ")