def tichso(n):
    tich = 1
    for i in range(len(n)):
        if int(n[i])!=0:
            tich *= int(n[i])
    return tich
		
t = int(input())
while t > 0:
    print(tichso(input()))
    t-=1
