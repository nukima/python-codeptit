n = int(input())
a = input().split()
a = [int(i) for i in a]

prime = [True for i in range(1000000)]
prime[0] = False
prime[1] = False
for i in range(2,1001):
    if prime[i] == True:
        for j in range(i**2, 1000000,i):
            prime[j] = False

for i in range(n):
    if prime[a[i]] == True:
        cnt = 1
        for j in range(i+1, n):
            if a[j] == a[i]:
                cnt += 1
        prime[a[i]] = False
        print(f"{a[i]} {cnt}")