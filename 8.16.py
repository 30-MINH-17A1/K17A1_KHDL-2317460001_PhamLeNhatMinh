a =int(input("nhập vào số nguyên a:"))
b =int(input("nhập vào số nguyên b:"))
while b:
    a, b = b, a%b
ucln = a
print("Ước chung lớn nhất của a và b là:" , ucln)