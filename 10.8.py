from datetime import datetime
from calendar import monthrange
n = int(input("Nhập vào ngày thứ: "))
m = int(input("Nhập vào tháng: "))
l = int(input("Nhập vào năm: "))
print(f"hôm nay là ngày {n}/{m}/{l}")
if datetime(l,m,n).month == 2:
    print(f"{l} không phải năm nhuận")
else:
    print(f"{l} là năm nhuận")
day_in_month = monthrange(l,m)[1]
print(f"Tháng {m} năm {l} có {day_in_month} ngày")