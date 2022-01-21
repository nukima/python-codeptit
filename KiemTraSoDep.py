def run(n: str):
    if len(set(n)) != 2:
        return "NO"
    for i in range(0, len(n) - 2):
        if n[i] != n[i + 2]:
            return "NO"
    return "YES"


for _ in range(int(input())):
    print(run(input()))
