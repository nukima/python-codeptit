def solve():
    t = int(input())
    while t!=0:
        s = input()
        d = 1 
        for i in range(0, len(s)-1):
            if s[i] == s[i+1]:
                d+=1;
            
            else:
                print(d,end=""+s[i])
                d = 1
        print(d,end=""+s[len(s)-1])
        print()
        t-=1
if __name__ == "__main__":
    solve()