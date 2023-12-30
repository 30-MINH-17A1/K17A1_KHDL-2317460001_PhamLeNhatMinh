A=[]
while True:
    gia_tri=int(input("nhập giá trị:\n"))
    A.append(gia_tri)
    tiep_tuc=input("thêm giá trị 1:đồng ý, 0:dừng\n")
    if tiep_tuc!='1':
        break
so_am = [num for num in A if num < 0 ]
so_duong = [num for num in A if num > 0 ]
print("số âm trong list là: ", so_am)
sum_am = sum(so_am)
sum_duong = sum(so_duong)
pt_so_am = len(so_am)
pt_so_duong = len(so_duong)
trung_binh_am = sum_am / pt_so_am
trung_binh_duong = sum / pt_so_duong
print("trung bình cộng các phần tử âm là: ", trung_binh_am )
print("trung bình cộng các phần tử dương là: ", trung_binh_duong )
max = max(A)
min = min(A)
print(f"max A là {max}")
print(f"min của A là {min}")
up = sorted(A)
print("danh sách tăng dần là:", up)