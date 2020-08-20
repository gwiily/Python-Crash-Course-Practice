filename = r'learning_python.txt'

with open(filename) as learning_python:
	for line in learning_python:
		line = line.rstrip()
		print(line.replace('Python', 'C'))