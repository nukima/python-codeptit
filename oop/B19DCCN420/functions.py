def is_valid(txt: str):
    lwr = "abcdefghijklmnopqrstuvwxyz"
    upr = lwr.upper()
    digits = "0123456789"
    special = "$#@"
    valid_criterial = 0
    for chr in lwr:
        if chr in txt:
            valid_criterial += 1
            break
    for chr in upr:
        if chr in txt:
            valid_criterial += 1
            break
    for chr in digits:
        if chr in txt:
            valid_criterial += 1
            break
    for chr in special:
        if chr in txt:
            valid_criterial += 1
            break
    if len(txt) <= 12 and len(txt) >= 6:
        valid_criterial += 1
    return valid_criterial == 5


for i in range(int(input())):
    valid = ""
    passwords = input().split(",")
    for password in passwords:
        if is_valid(password):
            valid = valid + password + ","
    print(valid[:-1])
