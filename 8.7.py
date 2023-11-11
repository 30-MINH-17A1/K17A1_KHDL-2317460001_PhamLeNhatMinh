a = int(input("nhập vào số kwh:"))
if a <= 50:
    tien_dien = a * 1.678
elif a <=100:
    tien_dien = a * 1.734
elif a <=200:
    tien_dien = a * 2.014
elif a <=300:
    tien_dien = a * 2.536
elif a <=400:
    tien_dien = a * 2.834
else:
    tien_dien = a * 2.927
print(" số tiền điện phải trả là:", tien_dien)