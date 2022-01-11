import math

def isPrime(n):
    if n<=1: return False
    if n<=3: return True
    if n%2==0 or n%3==0: return False
    for i in range(5,int(math.sqrt(n))+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True

def tn(n):
    n = str(n)
    n = n[::-1]
    return int(n)

t = int(input())
while t > 0:
    s = int(input())
    if math.gcd(s,tn(s))==1:
        print("YES")
    else:
        print("NO")
    t-=1