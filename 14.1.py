def kiem_tra_tam_giac(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Tam giác đều"
        elif a == b or a == c or b == c:
            return "Tam giác cân"
        else:
            return "Tam giác thường"
    else:
        raise ValueError("Ba cạnh không tạo thành một tam giác")
try:
    a = float(input("Nhập độ dài cạnh a: "))
    b = float(input("Nhập độ dài cạnh b: "))
    c = float(input("Nhập độ dài cạnh c: "))   
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Độ dài cạnh phải là số dương và khác 0.") 
    loai_tam_giac = kiem_tra_tam_giac(a, b, c)
    print(f"Đây là một tam giác {loai_tam_giac}")
except ValueError as e:
    print(f"Lỗi: {e}")
except Exception as e:
    print(f"Lỗi không xác định: {e}")