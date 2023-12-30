def tinh_tien_dien(kwh):
    if kwh <= 50:
        tien_dien = kwh * 1.678
    elif kwh <= 100:
        tien_dien = kwh * 1.734
    elif kwh <= 200:
        tien_dien = kwh * 2.014
    elif kwh <= 300:
        tien_dien = kwh * 2.536
    elif kwh <= 400:
        tien_dien = kwh * 2.834
    else:
        tien_dien = kwh * 2.927
    return tien_dien
so_kwh = float(input("Nhập vào số kwh: "))
so_tien_dien = tinh_tien_dien(so_kwh)
print("Số tiền điện phải trả là:", so_tien_dien)