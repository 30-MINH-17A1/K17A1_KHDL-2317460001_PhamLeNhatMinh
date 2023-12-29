def ghi_noi_dung_vao_tap_tin(name, new):
    try:
        try:
            with open(name, 'r', encoding='utf-8') as file_old:
                old= file_old.read()
        except FileNotFoundError:
            old = None
        with open(name, 'a', encoding='utf-8') as file:
            if old is not None:
                file.write('\n')
            file.write(new)
        print(f"Đã ghi nội dung vào tập tin '{name}'.")
    except Exception as e:
        print(f"Lỗi: {e}")
def tiep_tuc():
    while True:
        choice = input("Bạn muốn tiếp không? (Chọn 1 để tiếp tục, 0 để dừng lại): ")
        if choice == '1':
            return True
        elif choice == '0':
            return False
        else:
            print("Chọn không hợp lệ. Vui lòng chọn lại.")
while True:
    name = input("Nhập tên tập tin có sẵn trong VSCode: ")
    new = input("Nhập nội dung muốn thêm vào tập tin: ")
    ghi_noi_dung_vao_tap_tin(name, new)
    if not tiep_tuc():
        break