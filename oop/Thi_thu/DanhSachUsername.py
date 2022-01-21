t = int(input())
username_list = []
filtered = []
for _ in range(t):
    username_list.append(input().lower())
for name in set(username_list):
    if username_list.count(name) > 1:
        filtered.append(name)
for name in sorted(filtered):
    print(name)

"""
nguyenmanhson
sonnm
NGUYENMANHSON
SonNM
NguyenManhSon
"""
