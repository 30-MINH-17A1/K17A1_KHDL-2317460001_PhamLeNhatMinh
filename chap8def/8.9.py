import time
def dem_nguoc(n):
    while n > 0:
        print(n)
        time.sleep(1)
        n -= 1
    print("Đến ngày")
so_ngay = float(input("Nhập số ngày cần đếm ngược: "))
dem_nguoc(so_ngay)