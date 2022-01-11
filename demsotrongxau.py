t = int(input())
while t > 0:
    s = input()
    n = input()
    res = 0
    i = 0
    while i + len(n) < len(s) + 1: 
        if s[i:i+len(n)] == n:
            i = i + len(n)
            res += 1

        i += 1
            
    print(res)
    
    t -= 1 