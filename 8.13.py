import math
n = int(input("Nhập vào số nguyên n:"))
A = sum(i for i in range(1, n) if i % 2 != 0)
B = sum(i for i in range(1, n) if i % 2 == 0)
C = 1
for i in range (1, n+1):
    C *= i
D = 1
for i in range (1,  n+1):
    if i % 3 ==0:
        D *= i
E = sum(i for i in range(2,n+1) if all(i % j != 0 for j in range(2,int(i**0.5)+1)))
F = sum((-1)**i * i for i in range(1,n+1))
print("A =", A)
print("B =", B)
print("C =", C)
print("D =" ,D)
print("E =" ,E)
print("F =" ,F)