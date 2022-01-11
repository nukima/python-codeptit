
a = int(input())
while a > 0:
    n = input()
    s, t = 0, 1
    dem = 0
    x = 0
    for i in range(len(n)):
        if i%2==0:
            s += int(n[i])
        elif i%2!=0 :      
            x += 1
            if int(n[i])!=0:
                t *= int(n[i])
            elif int(n[i])==0:
                dem += 1
    
    if dem == x:
        t = 0
    res = str(s) + " " + str(t)
    print(res)
    
    a -= 1 