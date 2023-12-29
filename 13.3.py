def ghi_noi_dung_vao_tap_tin(old, new):
    try:
        with open('rain.txt', 'w', encoding= 'utf-8') as f:
            f.write("Rain rain, go away: Come again another day\n")
            f.write("Rain rain : Come \n")
        print(f"Đã ghi nội dung mới vào tập tin '{old}'.")
    except Exception as e:
        print(f"Lỗi: {e}")
new = "Hello, this is the new content!\n"
ghi_noi_dung_vao_tap_tin('rain.txt', new)