import math
def giải_pt_bậc2(a,b,c):
    Delta = pow(b,2)-4*a*c
    if Delta < 0:
        return "Phương trình vô nghiệm"
    elif Delta == 0:
        x = -b/(2*a)
        return f"Phương trình có nghiệm kép x = {x}"
    else:
        x1 = math.sqrt((Delta)/(2*a))
        x2 = math.sqrt((Delta)/(2*a))
        return f"Phương trình có 2 nghiệm phân biệt {x1} và {x2}"
a = float(input("Nhập vào số a: "))
b = float(input("Nhập vào số b: "))
c = float(input("Nhập vào số c: "))
print("",giải_pt_bậc2(a,b,c))