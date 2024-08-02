age = 16

is_conNit = False  # default # initialise the variable
if age < 10:
	is_conNit = True

if is_conNit:
	print("tre nho")
elif age < 18:
	print("thieu nien")
	if 15 <= age <= 17:
		print("thanh thieu nien")
else:
	print("nguoi lon")
