filename = "guest.txt"

name = input("Please input your name:\n")
with open(filename, 'w') as guest:
	guest.write(name + "\n")