class Matrix:
    def __init__(self, n, m, matrix=None):
        self.n = n
        self.m = m
        self.matrix = matrix
        if matrix is None:
            self.matrix = [[0 for i in range(m)] for j in range(n)]

    def getTranspose(self):
        matrix_tmp = [list(i) for i in zip(*self.matrix)]
        tmp = Matrix(self.m, self.n, matrix_tmp)
        return tmp

    def __str__(self):
        strings = []
        for row in self.matrix:
            strings.append(" ".join(str(x) for x in row))
        return "\n".join(strings)

    def __mul__(self, other):
        result = Matrix(n, n)
        for i in range(self.n):
            for j in range(other.m):
                for k in range(other.n):
                    result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return result


t = int(input())
for _ in range(t):
    n, m = [int(x) for x in input().split()]
    tmp = []
    for _ in range(n):
        tmp.append([int(x) for x in input().split()])
    matrix_1 = Matrix(n, m, tmp)
    matrix_1_t = matrix_1.getTranspose()
    result = matrix_1 * matrix_1_t
    print(result)
