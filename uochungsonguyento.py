import math
def check(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def tcs(n):
    sum = 0
    for i in n:
        sum += ord(i) - ord('0')
    return sum

t = int(input())
while (t > 0):
    t -= 1
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    c = math.gcd(a,b)
    d = tcs(str(c))
    
    if check(d):
        print("YES")
    else:
        print("NO")