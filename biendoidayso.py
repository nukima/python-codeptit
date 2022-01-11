def checkkq(a):
    for i in range(3):
        if a[i]!=a[i+1]: return False
    return True

while True:
    s = input()
    if s=="0 0 0 0": break
    else:
        a = [int(i) for i in s.split()]
        dem = 0
        while checkkq(a)==False:
            dem += 1
            x = a[0]
            a[0] = abs(a[0] - a[1])
            a[1] = abs(a[1] - a[2])
            a[2] = abs(a[2] - a[3])
            a[3] = abs(a[3] - x)

        print(dem)