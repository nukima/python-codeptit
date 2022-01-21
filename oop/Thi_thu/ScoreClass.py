class ThiSinh:
    def __init__(self, hoTen, chuyenCan, baiTapLon, cuoiKy):
        self.hoTen = hoTen
        self.chuyenCan = chuyenCan
        self.baiTapLon = baiTapLon
        self.cuoiKy = cuoiKy
        self.tongDiem = chuyenCan * 0.1 + baiTapLon * 0.3 + cuoiKy * 0.6

    def __str__(self):
        strings = f"{self.hoTen} {self.tongDiem:.1f}"
        return strings


ts1 = ThiSinh(input(), float(input()), float(input()), float(input()))
print(ts1)
""" 
Nguyen Van A
10
7
8
"""
