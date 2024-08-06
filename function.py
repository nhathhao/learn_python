# # def print_letter():
# # 	print("a")
# # 	print("b")
# # 	print("c")
# # print_letter()
#
# def print_number(min_munber, max_number, distance):
# 	for i in range(min_munber, max_number, distance):
# 		print(i)
#
#
# min_num = input("Số bắt đầu: ")
# max_num = input("Giới hạn của dãy số: ")
# dis = input("Khoảng cách các số: ")
# print_number(int(min_num), int(max_num), int(dis))
#
# def add_one(number):
# 	number += 1
# 	return number
#
#
# x = 2
# x = add_one(x)
# print(x)
def main():
	tenA = "Hao"
	toanA = 9
	vanA = 7

	tenB = "Quang"
	toanB = 8
	vanB = 9

	print_hocsinh(tenA, toanA, vanA)
	print_hocsinh(tenB, toanB, vanB)


def print_hocsinh(ten, diemToan, diemVan):
	print("Ten: " + ten)
	print("Toan: " + str(diemToan))
	print("Van: " + str(diemVan))


main()