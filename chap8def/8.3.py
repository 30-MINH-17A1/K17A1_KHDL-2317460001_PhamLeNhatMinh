def giai_phuong_trinh_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            return "vô số nghiệm"
        else:
            return "vô nghiệm"
    else:
        return "phương trình có nghiệm = " + str(-b/a)
a = float(input("Nhập vào một số a: "))
b = float(input("Nhập vào một số b: "))
ket_qua = giai_phuong_trinh_bac_nhat(a, b)
print(ket_qua)