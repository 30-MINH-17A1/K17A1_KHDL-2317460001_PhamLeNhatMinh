def find_max(a, b, c, d):
    max = a
    if max < b : max =b
    if max < c : max =c
    if max < d : max =d
    return max
a=int(input("nhập vào số thứ nhất:"))
b=int(input("nhập vào số thứ hai:"))
c=int(input("nhập vào số thứ ba:"))
d=int(input("nhập vào số thứ tư:"))
print("số lớn nhất trong 4 số ", a,";", b, ";", c, ";", d, ";", " là ", find_max(a, b, c, d))