def tinh_tong_n_so_nguyen(n):
    tong = 0
    for i in range(n):
        so_nguyen = int(input(f"Nhập số nguyên thứ {i+1}: "))
        tong += so_nguyen
    return tong
so_luong_so_nguyen = int(input("Nhập số lượng số nguyên n: "))
tong_tat_ca_so_nguyen = tinh_tong_n_so_nguyen(so_luong_so_nguyen)
print(f"Tổng của {so_luong_so_nguyen} số nguyên là: {tong_tat_ca_so_nguyen}")