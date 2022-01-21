def run(num: str):
    for char in num:
        if char not in digit:
            return "NO"
    return "YES"


digit = ["0", "1", "2"]
for _ in range(int(input())):
    print(run(input()))
