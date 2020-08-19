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


liming = User("Li", "Ming", "male")
print(liming.login_attempts)
liming.increment_login_attempts()
liming.increment_login_attempts()
liming.increment_login_attempts()
liming.increment_login_attempts()
print(liming.login_attempts)
liming.reset_login_attempts()
print(liming.login_attempts)