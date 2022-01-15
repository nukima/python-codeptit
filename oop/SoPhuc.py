class SoPhuc:
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return SoPhuc(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return SoPhuc(
            self.real * other.real - self.imag * other.imag,
            self.imag * other.real + self.real * other.imag,
        )

    def __str__(self):
        strings = ""
        if self.imag > 0:
            strings = f"{self.real:.0f} + {self.imag:.0f}i"
        elif self.imag < 0:
            strings = f"{self.real:.0f} - {abs(self.imag):.0f}i"
        else:
            strings = f"{self.real:.0f}"
        return strings


for _ in range(int(input())):
    inp = [float(num) for num in input().split()]
    a = SoPhuc(inp[0], inp[1])
    b = SoPhuc(inp[2], inp[3])
    c = (a + b) * a
    d = (a + b) * (a + b)
    print(c, d, sep=", ")
