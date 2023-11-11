def is_prime(x):
    if x <= 1:
        return False
    for i in range (2,x):
        if x % i == 0:
            return False
        return True
x = int(input("nhập vào một số x:"))
if is_prime(x):
    print((x), " là số nguyên tố")
else:
    print((x), " không là số nguyên tố")