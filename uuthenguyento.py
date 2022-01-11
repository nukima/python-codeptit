import math

def isPrime(n):
    if n<=1: return False
    if n<=3: return True
    if n%2==0 or n%3==0: return False
    for i in range(5,int(math.sqrt(n))+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True

def checkuuthenguyento(n):
    nt = 0
    not_nt = 0
    for i in range(len(n)):
        if isPrime(int(n[i]))==False:
            not_nt += 1
        elif isPrime(int(n[i])):
            nt += 1
    return nt > not_nt and isPrime(len(n))

t = int(input())
while t > 0:
    s = input()
    if checkuuthenguyento(s):
        print("YES")
    else:
        print("NO")
    t-=1
