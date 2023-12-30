def tinh_tien_cuoc(loai_xe, so_km, so_phut_cho):
    if loai_xe == 4:
        gia_mo_cua = 11.000
    elif loai_xe == 7:
        gia_mo_cua = 13.000
    if loai_xe == 4 and so_km <= 20:
        tien_di_chuyen = 12.100 * so_km + gia_mo_cua
    elif loai_xe == 7 and so_km <= 30:
        tien_di_chuyen = 14.100 * so_km + gia_mo_cua
    else:
        tien_di_chuyen = 10.000 * so_km + gia_mo_cua
    tien_cho = 0 if so_phut_cho <= 5 else so_phut_cho * 0.8
    tien_cuoc = tien_cho + tien_di_chuyen
    return tien_cho, tien_di_chuyen, tien_cuoc
loai_xe = float(input("Nhập loại xe (4 or 7): "))
so_km = float(input("Nhập số km mà xe đi: "))
so_phut_cho = float(input("Nhập số phút chờ: "))
tien_cho, tien_di_chuyen, tien_cuoc = tinh_tien_cuoc(loai_xe, so_km, so_phut_cho)
print("Tiền chờ phải trả:", tien_cho, 'nghìn đồng')
print("Tiền di chuyển phải trả:", tien_di_chuyen, 'nghìn đồng')
print("Tiền cước phải trả:", tien_cuoc, 'nghìn đồng')