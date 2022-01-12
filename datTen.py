def name_gen(k, name_pool):
    if k == 1:
        return name_pool
    else:
        return [
            y + " " + x
            for y in name_gen(1, name_pool)
            for x in name_gen(k - 1, name_pool)
            if x > y
        ]


n, k = [int(x) for x in input().split()]
name_pool = list(set(input().split()))
name_pool = sorted(name_pool)
result = name_gen(k, name_pool)
result = sorted(result)
print(result)
