def Sum(n):
    string =str(n)
    sum = 0
    for i in string:
        sum += ord(i) - ord('0')
    return sum

n = int(input())
while n > 0:
    n -= 1
    m = int(input())
    arr = input().split()
    arr = [int(i) for i in arr]
    arr.sort()
    arr = [str(i) for i in arr]
    arr.sort(key=Sum)
    for x in arr:
        print(x, end=" ")
    print()