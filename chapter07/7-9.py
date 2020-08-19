sandwich_orders = ['a', 'pastrami', 'c', 'pastrami', 'e', 'pastrami']
finished_orders = []
print("Sorry, we're all out of pastrami today.\n")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
while sandwich_orders:
	current_orders = sandwich_orders.pop()
	print("I made your " + current_orders.title() + " sandwich!")
	finished_orders.append(current_orders)

print("\nThe following sandwich have been maded!")
for sandwich in finished_orders:
	print(sandwich)