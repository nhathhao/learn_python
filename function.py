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
	ten_hocsinh_a = "Hao"
	ten_hocsinh_b = "Quang"
	print_hocsinh_a(ten_hocsinh_a)
	print_hocsinh_b(ten_hocsinh_b)


def print_hocsinh_a(name):
	print("Hoc sinh A")
	print("Ten: " + name)
	print("Toan: 8")
	print("Van: 7")


def print_hocsinh_b():
	print("Hoc sinh A")
	print("Toan: 8")
	print("Van: 7")


main()