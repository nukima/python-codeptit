import math

def isPrime(n):
    if n<=1: return False
    if n<=3: return True
    if n%2==0 or n%3==0: return False
    for i in range(5,int(math.sqrt(n))+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True

def check(n):
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    return isPrime(sum)

def checkvitri(n):
    for i in range(len(n)):
        if i%2==0 and int(n[i])%2!=0:
            return False
        elif i%2!=0 and int(n[i])%2==0:
            return False
    return True
		
t = int(input())
while t > 0:
    s = input()
    if checkvitri(s) and check(s):
        print("YES")
    else:
        print("NO")
    t-=1