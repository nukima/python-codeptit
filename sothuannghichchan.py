def gen(stri):
    for i in range(0,9,2):
        char = str(i)
        tmp = char + stri + char
        a.append(tmp)
        if len(tmp) < 6:
            gen(tmp)

a = []
gen("")
b = []
for i in range (len(a)):
    if a[i][0] != '0':
        b.append(a[i])
b = [int(i) for i in b]
b.sort()

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    # index = 0
    # while a[index] < n:
    #     print(a[index], end=" ")
    #     index += 1
    for i in b:
        if i < n:
            print(i, end=" ")
    print()