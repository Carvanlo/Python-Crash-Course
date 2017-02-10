favorite_places = {
	'eric': ['bear moutain', 'death valley', 'tierra del fuego'],
	'erin': ['hawaii', 'iceland'],
	'ever': ['mt. verstovia', 'the playgournd', 'south carolina']
	}
	
for name, places in favorite_places.items():
	print("\n" + name.title() + " likes the following places:")
	for place in places:
		print("- " + place.title())
		
