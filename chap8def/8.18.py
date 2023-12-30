def kiem_tra_so_hoan_hao(n):
    tong_tat_ca_cac_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_tat_ca_cac_uoc += i
    return tong_tat_ca_cac_uoc == n
so_nguyen = int(input("Nhập vào một số nguyên: "))
ket_qua_kiem_tra = kiem_tra_so_hoan_hao(so_nguyen)
if ket_qua_kiem_tra:
    print(so_nguyen, "là số hoàn hảo.")
else:
    print(so_nguyen, "không là số hoàn hảo.")