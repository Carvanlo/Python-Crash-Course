def make_album(artist_name, album_title, track=''):
	"""Return a dictionary of information of an album."""
	album = {'artist': artist_name, 'title': album_title}
	
	if track:
		album['track'] = track
	return album
	
album_1 = make_album('Adam Levine', 'Begin Again', 3)
print(album_1)

album_2 = make_album('Emma Stevens', 'Enchanted')
print(album_2)

album_3 = make_album('Blake Shelton', 'Based on a True Story')
print(album_3)
