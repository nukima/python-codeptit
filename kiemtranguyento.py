import math
def check(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return (n > 1)

lis1 = input().split()
lis1 = [int(i) for i in lis1]
n = lis1[0]
m = lis1[1]
for i in range(n):
    a = input().split()
    a = [int(i) for i in a]
    for j in range (m):
        if check(a[j]) == True:
            print(1, end = " ")
        else:
            print(0, end = " ")
    print()
    
    
