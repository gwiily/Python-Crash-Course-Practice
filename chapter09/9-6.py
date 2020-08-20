# 餐厅类
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


# 继承的冰淇凌小店
class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type="ice_cream"):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = []


	def show_flavors(self):
		print("\nWe have the following flavors available:")
		for flavor in self.flavors:
			print("- " + flavor.title())


# 实例
Haagen_Dazs = IceCreamStand("Häagen-Dazs")
Haagen_Dazs.flavors = ['strawberry', 'chocolate', 'oreo']

Haagen_Dazs.describe_restaurant()
Haagen_Dazs.show_flavors()