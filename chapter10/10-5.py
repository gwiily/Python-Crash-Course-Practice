filename = 'love_coding.txt'

while True:
	content = input("Why do you love coding?(enter exit to quit)\n")
	if content == 'exit':
		break
	else:
		with open(filename, 'a') as love_coding:
			love_coding.write(content + '\n')