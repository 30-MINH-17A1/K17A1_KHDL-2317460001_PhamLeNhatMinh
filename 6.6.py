a = int(input("alice_candies:"))
b = int(input("bob_candies:"))
c= int(input("carol_candies:"))
so_keo_cua_moi_nguoi= a + b + c
so_keo_tung_ca_nhan = so_keo_cua_moi_nguoi // 3
to_smash = so_keo_cua_moi_nguoi % 3
print("Số kẹo mỗi người nhận được là:", so_keo_tung_ca_nhan)
print("Số kẹo dư sau khi chia là:", to_smash)