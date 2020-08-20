class User():
	def __init__(self, first_name, last_name, gender):
		self.first_name = first_name
		self.last_name = last_name
		self.gender = gender


	def describe_user(self):
		print(self.first_name + " " + self.last_name + " is a " + self.gender)


	def greet_user(self):
		print("Welcome to join us, " + self.last_name)


liming = User("Li", "Ming", "male")
print(liming.first_name)
print(liming.last_name)
print(liming.gender)
liming.describe_user()
liming.greet_user()


hanmeimei = User("Han", "Meimei", "female")
print(hanmeimei.first_name)
print(hanmeimei.last_name)
print(hanmeimei.gender)
hanmeimei.describe_user()
hanmeimei.greet_user()