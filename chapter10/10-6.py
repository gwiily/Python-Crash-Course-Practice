try:
	number_1 = input("Input the first number:")
	number_1 = int(number_1)
	number_2 = input("Input the second number:")
	number_2 = int(number_2)
except ValueError:
	print("Please input a number!")
else:
	result = number_1 + number_2
	print("The sum of " + str(number_1) + " and " + str(number_2) + " is " + str(result))
