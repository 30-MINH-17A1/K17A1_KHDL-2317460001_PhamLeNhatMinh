n = int(input("nhập số lượng số nguyên n:"))
tong = 0
for i in range(n):
    so_nguyen = int(input(f"Nhập số nguyên thứ {i+1} :"))
    tong += so_nguyen
print(f"tổng của {n} số nguyên là: {tong} ")