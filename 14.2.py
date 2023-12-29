class InputError(Exception):
    pass
def nhap_so_nguyen_duong():
    while True:
        try:
            so = int(input("Nhập một số nguyên dương (nhập 0 để kết thúc): "))
            
            if so == 0:
                break  
            elif so < 0:
                raise InputError("Lỗi: Nhập số âm.")
            elif so == nhap_so_nguyen_duong.so_truoc_1 == nhap_so_nguyen_duong.so_truoc_2 == nhap_so_nguyen_duong.so_truoc_3 == so:
                raise InputError("Lỗi: Nhập số giống nhau 4 lần liên tiếp.")
            elif not isinstance(so, int):
                raise InputError("Lỗi: Nhập số không phải là số nguyên.") 
            nhap_so_nguyen_duong.so_truoc_3 = nhap_so_nguyen_duong.so_truoc_2
            nhap_so_nguyen_duong.so_truoc_2 = nhap_so_nguyen_duong.so_truoc_1
            nhap_so_nguyen_duong.so_truoc_1 = so
        except ValueError:
            raise InputError("Lỗi: Nhập không phải là số nguyên.")
try:
    nhap_so_nguyen_duong.so_truoc_1 = nhap_so_nguyen_duong.so_truoc_2 = nhap_so_nguyen_duong.so_truoc_3 = None
    nhap_so_nguyen_duong()
    print("Kết thúc chương trình.")
except InputError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Lỗi không xác định: {e}")