import re

word_dict = {}

for _ in range(int(input())):
    line = input().lower().strip()
    line = re.sub("\d+", "", line)
    line = re.split("\W+", line)  # tra ve list
    for word in line:
        if word == "":
            continue
        word_dict[word] = word_dict.get(word, 0) + 1


result = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
for key, v in result:
    print(f"{key} {v}")
""" 
3
PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
voi muc ho tro 500000 dong/sinh vien PTIT.
"""
""" 
\w : a-zA-Z0-9_
\s : whitespace
\d : 0-9
"""
