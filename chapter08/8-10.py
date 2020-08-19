def show_magicans(magicians):
	print("list of magicians is:")
	for magician in magicians:
		print(magician)
		

def make_great(magicians):
	for magician in magicians:
		magician = 'the Great ' + magician
	print("Completed add the Great!")
	return magicians


magicians = ['magicianA', 'magicianB', 'magicianC']
make_great(magicians)
show_magicans(magicians)