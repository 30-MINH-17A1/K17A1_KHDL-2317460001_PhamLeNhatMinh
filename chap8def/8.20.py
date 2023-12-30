import math
def tinh_gia_tri_e_mu_x(x):
    ex = 1
    n = 1
    t = x
    while math.fabs(t) >= 0.0001:
        ex += t
        n += 1
        t *= (x / n)
    return ex
so_x = float(input("Nhập vào một số x: "))
ket_qua_gia_tri_e_mu_x = tinh_gia_tri_e_mu_x(so_x)
print("Giá trị gần đúng của e mũ x là:", ket_qua_gia_tri_e_mu_x)