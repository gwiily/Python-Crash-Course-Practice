class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0


	def describe_restaurant(self):
		print("This restaurant's name is " + self.restaurant_name + ". It's a " 
			+ self.cuisine_type +" restaurant.")


	def open_restaurant(self):
		print("This restaurant is open now")


	def increment_number_served(self, additiona_served):
		self.number_served += additiona_served


my_restaurant = Restaurant("HaiDiLao", "hotpot")
print(my_restaurant.number_served)
my_restaurant.number_served = 21
print(my_restaurant.number_served)
my_restaurant.increment_number_served(100)
print(my_restaurant.number_served)