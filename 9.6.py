def kiem_tra_so_nguyen_to(x):
    if x < 2:
        return False
    for i in range (2,x):
        if x % i == 0:
            return False
    return True
x  = int(input("Nhập vào số x: "))
result = kiem_tra_so_nguyen_to(x)
print("kết quả kiểm tra", kiem_tra_so_nguyen_to(x))