a = int(input("nhập vào một số a:"))
b = int(input("nhập vào một số b:"))
if a == 0 :
    if b == 0:
        print("vô số nghiệm")
    else:
        print("vô nghiệm")
else:
    print("phương trình có nghiêm = ", -b/a)