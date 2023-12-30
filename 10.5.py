def kiem_tra_ma_zip():
    ma_zip = input("Nhập mã zip: ")
    if len(ma_zip) != 6:
        return False
    for ky_tu in ma_zip:
        if not '0' <= ky_tu <= '9':
            return False
    return True
print(kiem_tra_ma_zip())