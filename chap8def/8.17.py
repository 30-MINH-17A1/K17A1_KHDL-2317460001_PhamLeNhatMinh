def tim_bcnn(a, b):
    mer_a, mer_b = a, b
    while mer_a != mer_b:
        if mer_a < mer_b:
            mer_a += a
        else:
            mer_b += b
    bcnn = mer_a
    return bcnn
so_a = int(input("Nhập vào số a: "))
so_b = int(input("Nhập vào số b: "))
ket_qua_bcnn = tim_bcnn(so_a, so_b)
print(f"Bội chung nhỏ nhất của {so_a} và {so_b} là: {ket_qua_bcnn}")