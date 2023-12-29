with open('humptyDumpty.txt', 'r') as f:
    HD = f.read()
    print("Nội dung file:")
    print(HD)
line_n = HD.count('\n')
char = len(HD)
print(f"số dòng là {line_n}")
print(f"số ký tự là {char}")