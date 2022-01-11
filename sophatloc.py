t = int(input())
while t!=0:
    n = input()
    if n[len(n)-1] == str(6) and n[len(n)-2] == str(8):
        print("YES")
    else:
        print("NO")
    t-=1