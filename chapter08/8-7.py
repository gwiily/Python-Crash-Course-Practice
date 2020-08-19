def make_album(name, album, amount=''):
	full_album = {"name":name, "album":album}
	if amount:
		full_album['amount'] = amount
	return full_album


full_album1 = make_album("song1", "album1")
full_album2 = make_album("song2", "album2", amount='10')
full_album3 = make_album("song3", "album3")

print(full_album1)
print(full_album2)
print(full_album3)