for i in range(0, 2):
	for j in range(3, 5):
		print(j)
		print(i)

print("\n ---- \n")

for i in range(10):
	if i == 5:
		continue
	print(i)

print("\n ---- \n")

for i in range(10):
	if i == 5:
		break
	print(i)

s_denominator = 0

for i in range(100):
	if i == 1:
		continue
	if i % 2 == 0:
		continue
	s_denominator += 1 / i

s = 1 / s_denominator
s = round(s, 2)
print(s)

s_denominator = 0

for i in range(3, 100, 2):
	if i == 1:
		continue
	s_denominator += 1 / i

s = 1 / s_denominator
s = round(s, 2)
print("S = " + str(s))

i = 0
while i < 10:
	print(i)
	i += 1
