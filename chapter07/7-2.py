# /usr/bin python3

i = True

while i:
	persons = int(input("How many persons to eat?\n"))
	if persons > 8:
		print("No empty tables.\n")
	else:
		print("Have a good dinner!")
		i = False
