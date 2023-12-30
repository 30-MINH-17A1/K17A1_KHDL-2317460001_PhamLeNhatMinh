import math
def tinh_A_B_C_D_E_F(n):
    A = sum(i for i in range(1, n+1) if i % 2 != 0)
    B = sum(i for i in range(1, n+1) if i % 2 == 0)
    C = math.factorial(n)
    D = 1
    for i in range(1, n+1):
        if i % 3 == 0:
            D *= i
    E = sum(i for i in range(2, n+1) if all(i % j != 0 for j in range(2, int(i**0.5)+1)))
    F = sum((-1)**i * i for i in range(1, n+1))
    return A, B, C, D, E, F
so_nguyen_n = int(input("Nhập vào số nguyên n: "))
ket_qua_A, ket_qua_B, ket_qua_C, ket_qua_D, ket_qua_E, ket_qua_F = tinh_A_B_C_D_E_F(so_nguyen_n)
print("A =", ket_qua_A)
print("B =", ket_qua_B)
print("C =", ket_qua_C)
print("D =", ket_qua_D)
print("E =", ket_qua_E)
print("F =", ket_qua_F)