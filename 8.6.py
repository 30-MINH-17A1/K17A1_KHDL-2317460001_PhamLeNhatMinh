a = int(input("nhập loại xe ( 4 or 7):"))
b = int(input("số km mà xe đi:"))
c = int(input("số phút chờ:"))
if a == 4:
    gia_mo_cua = 11.000
if a == 7:
    gia_mo_cua = 13.000
if a == 4 and b <= 20:
    tien_di_chuyen = 12.100 * b + gia_mo_cua
else:
    tien_di_chuyen = 10.000 * b + gia_mo_cua
if a == 7 and b <= 30:
    tien_di_chuyen = 14.100 * b + gia_mo_cua
else:
    tien_di_chuyen = 12.000 * b + gia_mo_cua
if c <= 5:
    tien_cho = 0
else:
    tien_cho = c * 0.8
tien_cuoc = tien_cho + tien_di_chuyen
print("tiền chờ phải trả :" , tien_cho ,'nghìn đồng')
print("tiền di chuyển phải trả :", tien_di_chuyen ,'nghìn đồng')
print("tiền cước phải trả :", tien_cuoc ,'nghìn đồng')