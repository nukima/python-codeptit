import math

def isPrime(n):
    if n<=1: return False
    if n<=3: return True
    if n%2==0 or n%3==0: return False
    for i in range(5,int(math.sqrt(n))+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True

t=int(input())
while t>0:
    n=int(input())
    k=0
    for i in range(1,n):
        if math.gcd(i,n)==1:
            k+=1
    if isPrime(k): print("YES")
    else: print("NO")
    
    t-=1