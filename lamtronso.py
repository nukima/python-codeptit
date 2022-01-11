def tron(n):
    a = []
    m = str(n)
    for i in range(len(m)):
        a.append(int(m[i]))
    a.reverse()
    for i in range(len(a)-1):
        if(a[i]>=5):
            a[i]=0
            a[i+1]+=1
        else:
            a[i]=0
    
    a.reverse()
    for i in a:
        print(i, end="") 

    print() 

t = int(input())
while t>0:
    n = int(input())
    tron(n)
    t-=1