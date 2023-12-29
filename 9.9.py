import math
r = float(input("Nhập vào bán kính r: "))
a = float(input("Nhập vào chiều dài hình chữ nhật a: "))
b = float(input("Nhập vào chiều rộng hình chữ nhật b: "))
pi = math.pi
Sc = lambda x, n : math.pow(r,2)*pi
Sr = lambda x, n : x*n
Pr = lambda x, n : x+n
Pc = lambda x, n : 2*pi*r
print("Diện tích hình tròn = ",Sc(r,pi))
print("Diện tích hình chữ nhật = ",Sr(a,b))
print("Chu vi hình tròn = ",Pc(r,pi))
print("Chu vi hình chữ nhật = ",Pr(a,b))