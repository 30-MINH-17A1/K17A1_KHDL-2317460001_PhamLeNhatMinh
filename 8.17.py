a =int(input("nhập vào số a:"))
b =int(input("nhập vào số b:"))
mer_a = a
mer_b = b
while mer_a != mer_b:
    if mer_a < mer_b:
        mer_a += a
    else:
        mer_b += b
bcnn = mer_a
print("Bội chung nhỏ nhất của hai số là:" ,bcnn)