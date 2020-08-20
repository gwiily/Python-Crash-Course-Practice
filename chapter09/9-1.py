class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type


	def describe_restaurant(self):
		print("This restaurant's name is " + self.restaurant_name + ". It's a " 
			+ self.cuisine_type +" restaurant.")


	def open_restaurant(self):
		print("This restaurant is open now")


chongqinghuoguo = Restaurant("chongqinghuoguo", "chinese food")
print(chongqinghuoguo.restaurant_name.title())
print(chongqinghuoguo.cuisine_type.title())
chongqinghuoguo.describe_restaurant()
chongqinghuoguo.open_restaurant()