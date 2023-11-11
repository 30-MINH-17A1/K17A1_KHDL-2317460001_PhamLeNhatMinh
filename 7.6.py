n = int(input("số tiền muốn đổi:"))
so_to_500000 = n // 500000
n %= 500000
so_to_200000 = n // 200000
n %= 200000
so_to_100000 = n // 100000
n %= 100000
so_to_50000 = n // 50000
n %= 50000
print("số tờ 500000 là: " ,so_to_500000)
print("số tờ 200000 là: " ,so_to_200000)
print("số tờ 100000 là: " ,so_to_100000)
print("số tờ 50000 là: " ,so_to_50000)
print("số tiền còn thừa" ,n)