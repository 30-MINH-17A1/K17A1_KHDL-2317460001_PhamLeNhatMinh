lst = []
while True:
    try:
        x = int(input("Nhập vào giá trị "))
        break
    except ValueError:
            print("Bị lỗi")
print("X =",x)