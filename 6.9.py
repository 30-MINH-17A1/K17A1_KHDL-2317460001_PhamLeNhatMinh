lai_suat_nam = float(input("Nhập lãi suất hàng năm (%): ")) / 100
so_tien_gui = float(input("Nhập số tiền gửi (VNĐ): "))
so_thang_gui = int(input("Nhập số tháng gửi: "))
tien_lai = (so_tien_gui * so_thang_gui) * (lai_suat_nam / 12)
tong_so_tien = so_tien_gui + tien_lai
print(f"Tiền lãi: {tien_lai:.0f} VNĐ")
print(f"Tổng số tiền sau {so_thang_gui} tháng: {tong_so_tien:.0f} VNĐ")