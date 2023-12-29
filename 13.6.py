import csv
def mo_file_csv(namecsv, ds_sdt, ds_name):
    try:
        with open(namecsv, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['SDT', 'Ten'])
            for sdt, ten in zip(ds_sdt, ds_name):
                writer.writerow([sdt, ten])
        print(f"Đã ghi nội dung vào tập tin '{namecsv}'.")
        hien_thi_noi_dung_csv(namecsv)
    except Exception as e:
        print(f"Lỗi: {e}")
def hien_thi_noi_dung_csv(namecsv):
    try:
        with open(namecsv, 'r', encoding='utf-8') as f:
            read = csv.reader(f)
            for row in read:
                print(row)
    except FileNotFoundError:
        print(f"Tập tin '{namecsv}' không tồn tại.")
    except Exception as e:
        print(f"Lỗi: {e}")
name = input("Nhập tên tập tin CSV: ")
ds_sdt = input("Nhập danh sách số điện thoại cách nhau bằng dấu phẩy: ").split(',')
ds_ten = input("Nhập danh sách tên cách nhau bằng dấu phẩy: ").split(',')
mo_file_csv(name, ds_sdt, ds_ten)