import math
def tinh_dien_tich_tam_giac(a, b, c):
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return S
a = float(input("Nhập vào giá trị cạnh a: "))
b = float(input("Nhập vào giá trị cạnh b: "))
c = float(input("Nhập vào giá trị cạnh c: "))
dien_tich = tinh_dien_tich_tam_giac(a, b, c)
print("Diện tích tam giác =", dien_tich)