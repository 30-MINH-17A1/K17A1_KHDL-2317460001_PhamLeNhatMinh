import math
a = float(input("Nhap do dai canh a: "))
b = float(input("Nhap do dai canh b: "))
c = float(input("Nhap do dai canh c: "))
p = (a+b+c)/2
S= math.sqrt(p* (p-a) * (p-b) * (p-c))
print("Dien tich cua tam giac la :" ,(S))