def số_hoàn_hảo(x):
    sum = 0
    for i in range(1, x):
        if x % i == 0:
            sum += i
    return sum == x
x = int(input("Nhập vào số x: "))
if số_hoàn_hảo(x):
    print(x, "Là số hoàn hảo")
else:
    print(x, "Không phải số hòan hảo")
