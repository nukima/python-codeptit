t = int(input())
while (t > 0):
    t -= 1
    fl = 1
    n = input()
    for i in n:
        if i != '4' and i != '7':
            print("NO")
            fl = 0
            break
    if fl == 1:
        print("YES")
    
        