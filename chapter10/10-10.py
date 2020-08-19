filename = 'alice.txt'

try:
	with open(filename) as f:
		contents = f.read()
except FileNotFoundError:
	print("Can't find " + filename)
else:
	times = contents.lower().count('the')
	print("Word 'the' has been found " + str(times) + " times.")