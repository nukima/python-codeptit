class ThiSinh:
    def __init__(self, hoTen, ngaySinh, diem1, diem2, diem3):
        self.hoTen = hoTen
        self.ngaySinh = ngaySinh
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3
        self.tongDiem = diem1 + diem2 + diem3

    def __str__(self):
        strings = f"{self.hoTen} {self.ngaySinh} {self.tongDiem:.1f}"
        return strings


ts1 = ThiSinh(input(), input(), float(input()), float(input()), float(input()))

print(ts1)

''' 
Nguyen Hoang Ha
11/10/2001
4.5
10.0
5.5
'''