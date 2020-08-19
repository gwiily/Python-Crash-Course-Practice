import json

filename = "favor_number.txt"
try:
	with open(filename) as f:
		favor_number = json.load(f)
		print("I know your favorite number! It's " + str(favor_number)+ ".")
except FileNotFoundError:
	print("Sorry, you have not submit your favorite number.")
	favor_number = input("Input your favorite number:")
	favor_number = int(favor_number)
	with open(filename, 'w') as f:
		json.dump(favor_number, f)

