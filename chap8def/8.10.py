def tinh_ket_qua(n, x):
    S = (x**2 + 1)**n
    return S
so_n = float(input("Nhập vào số n: "))
so_x = float(input("Nhập vào số x: "))
ket_qua = tinh_ket_qua(so_n, so_x)
print("Kết quả:", ket_qua)