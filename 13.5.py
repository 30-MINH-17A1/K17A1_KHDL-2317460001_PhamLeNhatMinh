import csv
def mo_file_csv():
    with open('launch.csv', 'r', encoding='utf-8') as f:
        read = csv.reader(f)
        for row in read:
            print(row)
mo_file_csv()