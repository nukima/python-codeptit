def checkxenke(n):
    for i in range(0,len(n)-1,2):
        if n[i]!=n[i+2]:
            return False
    return True
		
t = int(input())
while t > 0:
    s = input()
    if s[0]!=s[1] and len(s)%2!=0 and checkxenke(s):
        print("YES")
    else:
        print("NO")
    t-=1
