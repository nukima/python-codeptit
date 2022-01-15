word_dict = []

f = open("DATA.in", mode="r")
for line in f:
    for word in line.strip().split():
        try:
            tmp = int(word)
            if tmp > 2147000000:
                word_dict.append(word)
        except:
            word_dict.append(word)
word_dict.sort()
print(*word_dict)
