def permute(n, s):
    if n == 1:
        return s
    else:
        return [y + x for y in permute(1, s) for x in permute(n - 1, s)]


def check(x):
    if x[-1] == "2":
        return False
    for i in ["2", "3", "5", "7"]:
        if i not in x:
            return False
    return True


# -----------------------
n = int(input())
for _ in range(4, n + 1):
    all_gen = permute(_, ["2", "3", "5", "7"])
    filtered = list(filter(check, all_gen))
    result = sorted(filtered, key=lambda x: int(x))
    print("\n".join(result))
