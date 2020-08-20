filename = "guest_book.txt"

while True:
	name = input("Please input your name(enter exit to quit):")
	if name == 'exit':
		break
	else:
		with open(filename, 'a') as guest_book:
			guest_book.write(name+"\n")