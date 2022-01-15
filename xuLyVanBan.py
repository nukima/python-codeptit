import sys
import re

# text = ''
# while True:
#     try:
#         str = input()
#         text += str + " "
#     except EOFError:
#         break
txt = sys.stdin.read()
lines = re.split("\.|\?|\!", txt)
for line in lines:
    if line == "\n":
        continue
    line = line.strip()
    line = line.lower()
    line = line.replace('\n', '')
    line = line.capitalize()
    print(' '.join(line.split()))
