sandwich_orders = ['a', 'b', 'c', 'd', 'e']
finished_orders = []

while sandwich_orders:
	current_orders = sandwich_orders.pop()
	print("I made your " + current_orders.title() + " sandwich!")
	finished_orders.append(current_orders)

print("\nThe following sandwich have been maded!")
for sandwich in finished_orders:
	print(sandwich)