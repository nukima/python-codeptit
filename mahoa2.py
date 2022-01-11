def solve():

    P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    while True:
        k = input().split()
        d = 0
        if (int(k[0]) == 0):
            break
        K = int(k[0])

        s = k[1]
        x = ""
        for i in range(0,len(s)):
            if s[i] == '.':
                pre = 92
            elif s[i] == '_':
                pre = 91
            else:
                pre = ord(s[i])
            x1 = pre - ord('A')
            x1 = (x1 + K) % 28
            x += P[x1]
        print(x[::-1])


if __name__ == "__main__":
    solve()