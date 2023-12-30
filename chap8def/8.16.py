def tim_ucln(a, b):
    while b:
        a, b = b, a % b
    ucln = a
    return ucln
so_nguyen_a = int(input("Nhập vào số nguyên a: "))
so_nguyen_b = int(input("Nhập vào số nguyên b: "))
ket_qua_ucln = tim_ucln(so_nguyen_a, so_nguyen_b)
print(f"Ước chung lớn nhất của {so_nguyen_a} và {so_nguyen_b} là: {ket_qua_ucln}")