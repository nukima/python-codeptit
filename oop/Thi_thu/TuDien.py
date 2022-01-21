num_word = 0
dict_word = {}
for i in range(int(input())):
    for word in input().split(" "):
        word = word.lower()
        dict_word[word] = dict_word.get(word, 0) + 1
        num_word += 1

dict_word = sorted(dict_word.items(), key=lambda x: (-x[1], x[0]))
for k, v in dict_word:
    print(f"{k} {v / num_word:.2f}")

""" 
9
hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme
"""
