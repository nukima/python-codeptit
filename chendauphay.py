n = input()
n = n[::-1]
res = ""
for i in range(len(n)):
    if i % 3 == 2 and i < len(n) - 1:
        res += n[i] + ","
    else:
        res += n[i]
res = res[::-1]
print(res)