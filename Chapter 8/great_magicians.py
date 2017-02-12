magicians = ['David', 'melo', 'james']

def show_magicians(magicians):
	for magician in magicians:
		print(magician)

def make_great(magicians,):
	great_magicians = []

	while magicians:
		current_magician = magicians.pop()
		current_magician = "the Great to " + current_magician
		great_magicians.append(current_magician)
	
	for great_magician in great_magicians:
		magicians.append(great_magician)

show_magicians(magicians)
print("\n")
		
make_great(magicians)
show_magicians(magicians)		
