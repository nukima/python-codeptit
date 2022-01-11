def solve():
    t = int(input());
    while t!=0:
        n = int(input())
        lst = input().split()
        lst = [int(i) for i in lst]
        a = lst
        lst1 = input().split()
        lst1 = [int(i) for i in lst1]
        b = lst1
        k=0
        a.sort()
        b.sort()
        for i in range(0,n):
            if a[i]>b[i]:
                k=1
                break
        if(k==0): 
            print("YES") 
        else: 
            print("NO")     
        t-=1

if __name__ == "__main__":
    solve()