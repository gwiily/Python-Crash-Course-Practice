from user import User
# 权限类
class Privileges():
	def __init__(self, privileges=[]):
		self.privileges = privileges

	def show_privileges(self):
		print("\nThis Admin have the following privileges:")
		for privilege in self.privileges:
			print("- " + privilege)

	def add_privileges(self, privileges):
		self.privileges.extend(privileges)


# 继承的Admin类
class Admin(User):
	def __init__(self, first_name, last_name, gender):
		super().__init__(first_name, last_name, gender)
		self.privileges = Privileges()


