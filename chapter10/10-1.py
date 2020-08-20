filename = r'learning_python.txt'

# 第一次打印
print("- The first print:")
with open(filename) as learning_python:
	contents = learning_python.read()

print(contents)

# 第二次打印
print("- The second print:")
with open(filename) as learning_python:
	for line in learning_python:
		print(line.rstrip())

# 第三次打印
print("- The third print:")
with open(filename) as learning_python:
	lines = learning_python.readlines()

for line in lines:
	print(line.rstrip())