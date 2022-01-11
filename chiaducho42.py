a = []
test = 10
while test > 0:
    data = input()
    base = data.split()
    test -= len(base) 
    for i in base:
        a.append(i)

a = [(int(i) % 42) for i in a]
b = set(a)
print(len(b))