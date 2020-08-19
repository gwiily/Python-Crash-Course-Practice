number = input("Please input a number!\n")
number = int(number)

if number % 10 == 0:
	print(str(number) + " is integral multiple of 10!")
else:
	print(str(number) + " is not integral multiple of 10!")