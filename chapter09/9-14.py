from random import randint

class Die():
	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		print("Your number is " + str(randint(1, self.sides)))


d6 = Die()
print("10 times roll of a 6-sides die:")
for roll_time in range(10):
	d6.roll_die()

d10 = Die(10)
print("10 times roll of a 10-sides die:")
for roll_time in range(10):
	d10.roll_die()

d20 = Die(20)
print("10 times roll of a 20-sides die:")
for roll_time in range(10):
	d20.roll_die()