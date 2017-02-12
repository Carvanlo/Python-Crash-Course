def make_album(artist_name, album_title):
	"""Return a dictionary of information of an album."""
	album = {'artist': artist_name, 'title': album_title}	
	return album

while True:
	print("Please enter an album's artist and title.")
	print("(enter 'q' at any time to quit)")
	
	artist = input("\nPlease enter an album's artist. ")
	if artist == 'q':
		break
		
	title = input("Please enter this album's title. ")
	if title == 'q':
		break
	
	album = make_album(artist, title)
	print(album)
	print("\n")
