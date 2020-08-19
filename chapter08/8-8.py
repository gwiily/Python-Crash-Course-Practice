def make_album(name, album):
	full_album = name + " is in " + album + "!"
	return full_album


while True:
	print("\nPlease enter a song, and it's album")
	print("(Enter 'q'at any time to quit)")

	name = input("song's name: ")
	if name == 'q':
		break


	album = input("song's album: ")
	if album == 'q':
		break

	full_album = make_album(name, album)
	print("\nHello, " + full_album + "!")