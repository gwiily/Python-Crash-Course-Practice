# User类
class User():
	def __init__(self, first_name, last_name, gender):
		self.first_name = first_name
		self.last_name = last_name
		self.gender = gender
		self.login_attempts = 0


	def describe_user(self):
		print(self.first_name + " " + self.last_name + " is a " + self.gender)


	def greet_user(self):
		print("Welcome to join us, " + self.last_name)


	def increment_login_attempts(self):
		self.login_attempts += 1


	def reset_login_attempts(self):
		self.login_attempts = 0


# 继承的Admin类
class Admin(User):
	def __init__(self, first_name, last_name, gender):
		super().__init__(first_name, last_name, gender)
		self.privileges = []


	def show_privileges(self):
		print("\nThis Admin have the following privileges:")
		for privilege in self.privileges:
			print("- " + privilege)


# 实例
liming = Admin("li", "ming", "male")
liming.privileges = ["can add post", "can delete post", "can ban user"]
liming.describe_user()
liming.show_privileges()