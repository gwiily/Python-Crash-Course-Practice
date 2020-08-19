while True:
	try:
		print("Enter 'q' to quit")

		number_1 = input("Input the first number:")
		if number_1=='q':
			break
		number_1 = int(number_1)

		number_2 = input("Input the second number:")
		if number_2=='q':
			break
		number_2 = int(number_2)
	except ValueError:
		print("Please input a number!")
	else:
		result = number_1 + number_2
		print("The sum of " + str(number_1) + " and " + str(number_2) + " is " + str(result))
