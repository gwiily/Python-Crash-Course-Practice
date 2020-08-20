prompt = "\nPlease input your age:"
prompt += "\n(Enter 'quit' to end this program.)"
active = True
while active:
	age = input(prompt)
	if age == 'quit':
		break
	elif int(age) < 3:
		price = 'free'
	elif int(age) < 12:
		price = '10 dollers'
	else:
		price = '15 dollers'
	print("Your price is " + price + "!")