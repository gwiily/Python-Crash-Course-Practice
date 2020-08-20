import json

favor_number = input("Input your favorite number:")
favor_number = int(favor_number)
filename = "favor_number.txt"

with open(filename, 'w') as f:
	json.dump(favor_number, f)