def tinh_tong_tien(so_dem_o, ma_loai_phong):
    gia_phong = {
        1: {'loai': 'Standard', 'gia_1_dem': 1260000},
        2: {'loai': 'Superior Garden View', 'gia_1_dem': 1550000},
        3: {'loai': 'Superior Ocean view', 'gia_1_dem': 1830000},
        4: {'loai': 'Garden View Bungalow', 'gia_1_dem': 1830000},
        5: {'loai': 'Pool View Bungalow', 'gia_1_dem': 2120000},
        6: {'loai': 'Family room', 'gia_1_dem': 2120000},
        7: {'loai': 'Beach Front Bungalow', 'gia_1_dem': 2540000},
        8: {'loai': 'Vip Sea View', 'gia_1_dem': 4800000},
    }
    loai_phong = gia_phong.get(ma_loai_phong)
    if not loai_phong:
        print("Mã loại phòng không hợp lệ.")
        return None
    he_so_giam_gia = 1.0
    if 2 <= so_dem_o <= 3:
        he_so_giam_gia = 0.75
    else:
        he_so_giam_gia = 0.7
    tong_tien = so_dem_o * loai_phong['gia_1_dem'] * he_so_giam_gia
    return tong_tien
so_dem_o = float(input("Nhập số đêm ở: "))
ma_loai_phong = float(input("Nhập mã loại phòng (1-8): "))
tong_tien = tinh_tong_tien(so_dem_o, ma_loai_phong)
if tong_tien is not None:
    print("Tổng tiền phải trả là:", tong_tien)