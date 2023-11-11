import math
x = int(input("nhập vào một số x:"))
ex = 1
n =1
t =x
while math.fabs(t)>=0.0001:
    ex += t
    n += 1
    t *=(x/n)
print("giá trị gần đúng của e mũ x là:" ,ex)