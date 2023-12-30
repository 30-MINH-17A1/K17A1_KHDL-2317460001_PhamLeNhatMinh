def in_day_so_dao_nguoc_le(n):
    reversed_num = list(range(n, 0, -1))
    print("Dãy số đảo ngược chỉ gồm số lẻ là:")
    for num in reversed_num:
        if num % 2 != 0:
            print("", num, end='')
so_goc_duong = int(input("Nhập vào một số gốc dương: "))
in_day_so_dao_nguoc_le(so_goc_duong)