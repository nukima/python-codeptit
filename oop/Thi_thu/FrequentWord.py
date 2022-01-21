from collections import Counter

counts = Counter([])
for _ in range(int(input())):
    counts += Counter(input().split())
word_freq = dict(counts)
freq_max = max(word_freq.values())
word_freq = {key: val for key, val in word_freq.items() if val < freq_max}
word_freq = dict(sorted(word_freq.items(), key=lambda x: (-x[1], x[0])))
freq_max = max(word_freq.values())
for key, value in word_freq.items():
    if value == freq_max:
        print(key, end=" ")

"""
4
apple orange banana
banana orange fruit
mango orange
mango
"""
