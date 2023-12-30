def kiem_tra_nam_nhuan(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        return "năm nhuận"
    else:
        return "năm không nhuận"
nam = float(input("Nhập vào năm cần kiểm tra: "))
ket_qua = kiem_tra_nam_nhuan(nam)
print(ket_qua)