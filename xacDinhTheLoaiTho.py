all_input = []
result = []
for _ in range(int(input())):
    all_input.append(input().split())

i = 0
while i < len(all_input):
    if len(all_input[i]) == 7:
        i += 4
        result.append(2)
        continue
    while i < len(all_input) and len(all_input[i]) != 7:
        i += 2
    result.append(1)

print(len(result))
for num in result:
    print(num)
""" 
Mot canh hai canh lai ba canh0
Tran troc ban khoan giac chang lanh
Canh bon canh nam vua chop mat
Sao vang nam canh mong hon bay
Minh ve minh co nho ta4
Muoi lam nam ay thiet tha man nong
Minh ve minh co nho khong6
Nhin cay nho nui nhin song nho nguon
8
"""
