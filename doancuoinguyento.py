import math

def isPrime(n):
    if n<=1: return False
    if n<=3: return True
    if n%2==0 or n%3==0: return False
    for i in range(5,int(math.sqrt(n))+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True

def checkdoancuoinguyento(n):
    n = str(n)
    return isPrime(int(n[len(n)-4:]))

t = int(input())
while t > 0:
    s = input()
    if checkdoancuoinguyento(s):
        print("YES")
    else:
        print("NO")
    t-=1
