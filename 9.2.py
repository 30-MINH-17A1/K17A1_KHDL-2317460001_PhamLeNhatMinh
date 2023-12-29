def tính_can(can):
    for i in range (1,10):
        if n == 0:
            return "Canh"
        elif n == 1:
            return "Tân"
        elif n == 2:
            return "Nhâm"
        elif n == 3:
            return "Quý"
        elif n == 4:
            return "Giáp"
        elif n == 5:
            return "Át"
        elif n == 6:
            return "Bính"
        elif n == 7:
            return "Đinh"
        elif n == 8:
            return "Mậu"
        else:
            return "Kỳ"
        can_name = tính_can(can)     
def tính_chi(chi):
    for i in range (1,12):
        if n == 0:
            return "Thân"
        elif n == 1:
            return "Dậu"
        elif n == 2:
            return "Tuất"
        elif n == 3:
            return "Hợi"
        elif n == 4:
            return "Tý"
        elif n == 5:
            return "Sửu"
        elif n == 6:
            return "Dần"
        elif n == 7:
            return "Mão"
        elif n == 8:
            return "Thìn"
        elif n == 9 :
            return "Tỵ"
        elif n == 10 :
            return "Ngọ"
        else :
            return "Mùi"
        chi_name = tính_chi(chi)        
n = int(input("Nhập vào năm cần chuyển đổi: "))
can = n %10
chi = n%12
print("Năm sau khi chuyển đổi là",tính_can(can) ,tính_chi(chi))