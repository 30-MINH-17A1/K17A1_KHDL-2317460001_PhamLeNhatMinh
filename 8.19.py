n = int(input("nhập vào một dãy số:"))
reversed_num = list(range(n, 0 , -1))
print("", reversed_num)
print("dãy số đảo ngược chỉ gồm số lẻ là:")
for num in reversed_num:
    if num % 2 !=0:
        print("", num)