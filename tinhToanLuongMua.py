from datetime import datetime as dt


class Tram:
    def __init__(self, ma, ten, time, mua):
        self.ma = ma
        self.ten = ten
        self.time = time
        self.mua = mua

    def getTb(self):
        return (self.mua / (self.time / 3600))

    def addTime(self, time):
        self.time += time

    def addMua(self, mua):
        self.mua += mua

    def __str__(self):
        return f"{self.ma} {self.ten} {self.getTb():.2f}"


tram_list = []
ten_list = []
ma = 1
for _ in range(int(input())):
    ten = input().strip()
    start = dt.strptime(input(), "%H:%M")
    end = dt.strptime(input(), "%H:%M")
    time = end - start
    time = time.total_seconds()
    mua = float(input())
    if ten not in ten_list:
        ten_list.append(ten)
        tmp = Tram("T{:02d}".format(len(ten_list)), ten, time, mua)
        tram_list.append(tmp)
    else:
        for tram in tram_list:
            if tram.ten == ten:
                tram.addTime(time)
                tram.addMua(mua)

for tram in tram_list:
    print(tram)

"""
10
Dong Anhn
07:30
08:00
60
Cau Giay
07:45
08:12
50
Soc Son
08:00
09:15
78
Dong Anh
18:50
20:00
88
Cau Giay
19:01
20:00
77
Soc Son
19:06
20:21
66
Dong Anh
21:00
21:40
49
Cau Giay
21:50
22:20
68
Dong Anh
22:15
23:45
30
Cau Giay
22:50
23:45
35
"""
