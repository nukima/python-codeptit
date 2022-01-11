from math import gcd
class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def rutGon(self):
        ucln = gcd(self.tu, self.mau)
        self.tu /= ucln
        self.mau /= ucln
    
    def __add__(self, other):
        total_tu = self.tu * other.mau + self.mau * other.tu
        total_mau = self.mau * other.mau
        return PhanSo(total_tu, total_mau)

    def __str__(self):
        return f'{int(self.tu)}/{int(self.mau)}'

inp = input().split()
ps1 = PhanSo(int(inp[0]), int(inp[1]))
ps2 = PhanSo(int(inp[2]), int(inp[3]))
ps = ps1 + ps2
ps.rutGon()
print(ps)