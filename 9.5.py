def tính_A(x,n):
    result = (x**2+1+x)**n + (x**2-x+1)**n
    return result
x = float(input("Nhập vào số x: "))
n = float(input("Nhập vào số n: "))
print("",tính_A(x,n))