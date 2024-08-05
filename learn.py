# Khai báo biến hằng
CURRENT_YEAR = 2024
METER_TO_FEET = 3.281

firstName = input("Your firstname: ")
lastName = input("Your lastname: ")
yearBorn = input("When you're born: ")
heightMeter = input("Your height (meter): ")

# Dùng vòng lặp while để buộc người dùng nhập đúng yêu cầu
while True:
	genderInput = input("Are you male (yes/no): ")
	if (genderInput == "yes") or (genderInput == "no"):
		break

yearBorn = int(yearBorn)  # Ép kiểu của biến về dạng integer vì input() nhập vào string

age = CURRENT_YEAR - yearBorn # Tính tuổi tới năm 2024 của người dùng

heightMeter = float(heightMeter)  # Ép kiểu của biến về dạng float vì input() nhập vào string
heightFeet = heightMeter * METER_TO_FEET
heightFeet = round(heightFeet, 1)  # Làm tròn đến 1 chữ số thập phân sau dấu phẩy

print("\n---")  # Cách ra 1 dòng
print("Your name is " + firstName + " " + lastName)
print("{2} is {0} years old in {1} ".format(age, CURRENT_YEAR, firstName))
print("You are " + str(heightFeet) + " feet tall")

is_male = None

# Dùng if_else để chuyển từ string input sang boolean true/false
if genderInput == "yes":
	is_male = True
else:
	is_male = False

if is_male is True:
	if heightFeet > 6.5:
		print("You are", end = " ")
		# Vòng lặp lại 10 lần chữ "very" bằng for
		for i in range(10):
			print("very", end = " ")
		print("tall as a man")
	elif heightFeet > 6.0:
		print("You are tall as a man")
	else:
		print("You are short as a man")

if is_male is False:
	if heightFeet > 5.7:
		print("You are tall as a girl")
	elif heightFeet < 5.0:
		print("You are", end = " ")
		# Vòng lặp lại 10 lần chữ "very" với while
		i = 0
		while i < 10:
			print("very", end = " ")
			i += 1
		print("short as a girl")
	else:
		print("You are short as a girl")
