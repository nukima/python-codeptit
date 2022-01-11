
a = int(input())
while a > 0:
    n = input()
    s, t = 0, 1
    for i in range(len(n)):
        if i%2==0 and int(n[i])!=0:
            t *= int(n[i])
        elif i%2!=0 :      
            s += int(n[i])
            
    res = str(t) + " " + str(s)
    print(res)
    
    a -= 1 