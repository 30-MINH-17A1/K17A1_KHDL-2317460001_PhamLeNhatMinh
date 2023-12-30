A = input("nhập các phần tử:").split(' ')
tuple = tuple(A)
print(tuple)
index_duong = int(input("nhập số từ 0 đến 9:"))
if index_duong > 9 :
    print("sai")
if index_duong < 0:
 print("với số nhỏ hơn không thì là trường hợp khác")
else:
 print("tuple=:" , tuple[index_duong])
index_am = int(input("nhập index từ -1 đến -9:"))
if index_am < -9 :
  print("index ngoài phạm vi yêu cầu")
if index_am > -1:
  print("index này của trường hợp trên:")
else:
  print("tuple=:", tuple[index_am] )
s_find = input("nhập chuỗi để xem nó xuất hiện bao lần: ")
dem = tuple.count(s_find)
print("phần tử s_find xuất hiện:", dem ,"lần") 