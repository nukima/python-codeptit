class MonHoc:
    def __init__(self, maMon, tenMon, thi):
        self.maMon = maMon
        self.tenMon = tenMon
        self.thi = thi

    def __str__(self):
        strings = f"{self.maMon} {self.tenMon} {self.thi}"
        return strings


monhoc_list = []
for _ in range(int(input())):
    tmp = MonHoc(input(), input(), input())
    monhoc_list.append(tmp)

monhoc_list = sorted(monhoc_list, key=lambda x: x.maMon)
for mon in monhoc_list:
    print(mon)

""" 
2
MUL1320
Nhap mon da phuong tien
Bai tap lon + Van dap truc tuyen
BAS1203
Giai tich 1
Thi viet + Van dap truc tuyen
"""
