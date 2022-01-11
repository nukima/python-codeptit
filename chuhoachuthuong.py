
s=input()
low = 0
up = 0
for i in s:
    if(i.islower()): low += 1 
    elif(i.isupper): up += 1

if(low<up): print(s.upper())
else: print(s.lower())