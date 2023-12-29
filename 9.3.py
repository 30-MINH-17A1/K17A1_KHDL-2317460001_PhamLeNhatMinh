def BMI(x):
    if x < 18.5:
        return "Gầy"
    elif x > 18.5 and x < 24.99:
        return "Bình thường"
    else:
        return "Thừa cân"
w = float(input("nhập vào cân nặng: "))
h = float(input("nhập vào chiều cao: "))
if h >= 5:
    print("vui lòng nhập lại só liệu!!!")
else:
    x = w/(h**2)
    result = BMI(x)
    print("Cân nặng:", w,"kg")
    print("Chiều cao:", h,"m")
    print("Thông qua chỉ số BMI cho thấy cơ thể bạn đang trong tình trạng ",BMI(x))