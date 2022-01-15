class SinhVien:
    def __init__(self, ten, dung, sub):
        self.ten = ten
        self.dung = dung
        self.sub = sub

    def __str__(self):
        return f"{self.ten} {self.dung} {self.sub}"


sv_list = []
for _ in range(int(input())):
    ten = input()
    dung, sub = [int(x) for x in input().split()]
    tmp = SinhVien(ten, dung, sub)
    sv_list.append(tmp)

sv_list = sorted(sv_list, key=lambda x: (-x.dung, x.sub, x.ten))
for sv in sv_list:
    print(sv)

""" 
2
Nguyen Van Nam
168 600
Tran Thi Ngoc
168 600
"""
