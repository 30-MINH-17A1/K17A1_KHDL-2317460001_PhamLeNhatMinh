def tinh_ket_qua(n, x):
    A = (x**2 + x + 1)**n + (x**2 - x + 1)**n
    return A
so_n = float(input("Nhập vào số n: "))
so_x = float(input("Nhập vào số x: "))
ket_qua = tinh_ket_qua(so_n, so_x)
print("Kết quả của biểu thức =", ket_qua)