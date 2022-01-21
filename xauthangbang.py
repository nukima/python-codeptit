def solve():
    t = int(input())
    while t != 0:
        n = input()
        x = 1
        n = [ord(x) for x in n]
        for i in range(0, len(n) // 2):
            if abs(n[i] - n[i + 1]) != abs(n[len(n) - 1 - i] - n[len(n) - i - 2]):
                print("NO")
                x = 0
                break
        if x == 1:
            print("YES")
        t -= 1


if __name__ == "__main__":
    solve()
