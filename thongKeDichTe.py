m, n = [int(_) for _ in input().split()]
matrix = []
for i in range(m):
    matrix.append([int(_) for _ in input().split()])
sum = 0
for i in range(m):
    for j in range(n):
        if matrix[i][j] == -1:
            # i-1 j-1
            if i - 1 >= 0 and j - 1 >= 0:
                if matrix[i - 1][j - 1] == -1:
                    sum += 0
                else:
                    sum += matrix[i - 1][j - 1]
                    matrix[i - 1][j - 1] = 0
            # i-1 j
            if i - 1 >= 0:
                if matrix[i - 1][j] == -1:
                    sum += 0
                else:
                    sum += matrix[i - 1][j]
                    matrix[i - 1][j] = 0
                # i-1 j+1
                if j + 1 < n:
                    if matrix[i - 1][j + 1] == -1:
                        sum += 0
                    else:
                        sum += matrix[i - 1][j + 1]
                        matrix[i - 1][j + 1] = 0
            # i j-1
            if j - 1 >= 0:
                if matrix[i][j - 1] == -1:
                    sum += 0
                else:
                    sum += matrix[i][j - 1]
                    matrix[i][j - 1] = 0
            # i j+1
            if j + 1 < n:
                if matrix[i][j + 1] == -1:
                    sum += 0
                else:
                    sum += matrix[i][j + 1]
                    matrix[i][j + 1] = 0
            # i+1 j-1
            if j - 1 >= 0 and i + 1 < m:
                if matrix[i + 1][j - 1] == -1:
                    sum += 0
                else:
                    sum += matrix[i + 1][j - 1]
                    matrix[i + 1][j - 1] = 0
            # i+1 j
            if i + 1 < m:
                if matrix[i + 1][j] == -1:
                    sum += 0
                else:
                    sum += matrix[i + 1][j]
                    matrix[i + 1][j] = 0
                # i+1 j+1
                if j + 1 < n:
                    if matrix[i + 1][j + 1] == -1:
                        sum += 0
                    else:
                        sum += matrix[i + 1][j + 1]
                        matrix[i + 1][j + 1] = 0


print(sum)

"""
1 1 0 1
2 -1 4 5
0 0 0 0
1 0 2 1
"""
