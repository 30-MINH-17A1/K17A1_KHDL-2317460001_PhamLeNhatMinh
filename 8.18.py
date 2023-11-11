n = int(input("Nhập vào một só nguyên:"))
tong_tat_ca_cac_uoc = 0
for i in range(1, n):
    if n % i == 0:
        tong_tat_ca_cac_uoc += i
if tong_tat_ca_cac_uoc == n:
    print(n, "là số hoàn hảo.")
else:
    print(n," không là số hoàn hảo.")