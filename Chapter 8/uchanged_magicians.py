def show_magicians(magicians):
	for magician in magicians:
		print(magician)

def make_great(magicians):
	great_magicians = []

	while magicians:
		current_magician = magicians.pop()
		current_magician = "the Great to " + current_magician
		great_magicians.append(current_magician)
	
	for great_magician in great_magicians:
		magicians.append(great_magician)
	
	return magicians
	
magicians = ['David', 'melo', 'james']

show_magicians(magicians)

print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)		

print("\nOriginal magicians:")
show_magicians(magicians)
