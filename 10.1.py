import math
n = int(input("nhập vào số lượng số để so sánh: "))
lst = []
for i in range(n):
    lst.append(float(input(f"Nhập vào giá trị thứ {i+1}: ")))
max_n =max(lst)
min_n = min(lst)
print("giá trị lớn nhất",max_n)
print("giá trị nhỏ nhất",min_n)
