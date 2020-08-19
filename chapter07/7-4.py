prompt = "\nPlease input a pizza ingredient:"
prompt += "\n(Enter 'quit' to end this.)"
active = True
while active:
	ingredient = input(prompt)
	if ingredient == 'quit':
		active = False
	else:
		print("\nWe will add the " + ingredient + "in to your pizza")