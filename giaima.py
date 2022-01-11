def solve():
    t = int(input());
    while t!=0:
        n = input()
        for i in range(0,len(n)):
            if n[i]>='1' and n[i]<='9':
                for j in range(0,int(n[i])):
                    print(n[i-1],end="")
        print("")
        t-=1

if __name__ == "__main__":
    solve()