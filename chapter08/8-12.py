def make_sandwich(*toppings):
    print("\nYour sandwich is following toppings:")
    for topping in toppings:
        print("- " + topping)


make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')