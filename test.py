# '''
#     Họ tên: Nguyễn Kim Mạnh
#     Mã SV: B19DCCN420
#     Sđt: 0345 521 329
# '''
# import math

# def isPrime(n):
#     prime_flag = 0
    
#     if(n > 1):
#         for i in range(2, int(math.sqrt(n)) + 1):
#             if (n % i == 0):
#                 prime_flag = 1
#                 break
#         if (prime_flag == 0):
#             return True
#         else:
#             return False
#     else:
#         return False


# def bai1():
#     '''
#         Viết chương trình tìm số nguyên tố thứ 30 và đếm số lượng số nguyên tố trong khoảng
#         từ 1 đến (30 + n) (Trong đó n là 1 chữ số cuối của Mã số sinh viên)
#     '''
#     print("Bai 1: ")
#     count, i = 0, 2
#     while count != 30:
#         if isPrime(i):
#             count += 1
#         i += 1
#     print("30th Prime Number:", i - 1)

#     count = 0
#     n = 0
#     for j in range(1, 30 + n + 1):
#         if isPrime(j):
#             count += 1
    
#     print(count)
#     print("-------------")
# #-----------
# def bai2():
#     '''
#         Viết một chương trình tính tổng các số tự nhiên chia hết cho n trong khoảng từ 1 đến
#         (200 + n) (có lấy giá trị 200 + n).
#         (Trong đó n là 1 chữ số cuối của Mã số sinh viên, nếu n = 0 thì lấy n = 10, nếu n=1 thì
#         lấy n=11)
#     '''
#     print("Bai 2: ")
#     n = 10
#     result = 0
#     for i in range(1, 200+n+1):
#         if i % n == 0:
#             result += i
#     print(result)
#     print("-------------")
# # --------------


# def bai3():
#     '''
#         Chỉ sử dụng hai dòng code để in ra
#     '''
#     print("Bai 3: ")
#     for i in range(5, 0, -1):
#         print('*' * (2*i - 1))
#     print("-------------")
# # --------------


# def isPerfectSquare(n):
#     root = math.sqrt(n)
#     if int(root + 0.5) ** 2 == n:
#         return True
#     return False

# def isPerfectCube(n):
#     root = n ** (1./3.)
#     if round(root) ** 3 == n:
#         return True
#     return False


# def bai4():
#     '''
#         Nhập một số từ bàn phím, in ra kết quả đó là số chính phương, số lập phương hay số tự
#         nhiên. Nếu số đó vừa là số chính phương, vừa là số lập phương, thì phải in ra cả hai.
#     '''
#     print("Bai 4: ")
#     n = int(input("Input Number: "))
#     check = True
#     if abs(n) == n:  
#         if isPerfectSquare(n):
#             print("Is Perfect Square Number")
#             check = False
#         if isPerfectCube(n):
#             print("Is Perfect Cube Number")
#             check = False
#     if check:
#         print("Is Natural Number") 
#     print("-------------")


# if __name__ == "__main__":
#     bai1()
#     bai2()
#     bai3()
#     bai4()

matrix = [[1,2,3],[3,1,2],[2,3,1]]
print(len(matrix))