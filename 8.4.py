import math
a = int(input("nhập vào giá trị cạnh a:"))
b = int(input("nhập vào giá trị cạnh b:"))
c = int(input("nhập vào giá trị cạnh c:"))
p = (a+b+c)/2
S = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Diện tích tam giác = ", S)