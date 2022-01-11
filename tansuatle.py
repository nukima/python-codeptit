t = int(input())
while t > 0:
    n = int(input())
    nums = input().split()
    nums = [int(num) for num in nums]
    result = 0
    for num in nums:
        result = result ^ num
    print(result)
    t -= 1