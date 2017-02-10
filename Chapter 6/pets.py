# Make an empty list
pets = []

ketty = {'kind': 'cat', 'owner': 'melo'}
pets.append(ketty)

doggy = {'kind': 'dog', 'owner': 'james'}
pets.append(doggy)

paul = {'kind': 'dog', 'owner': 'dwade'}
pets.append(paul)

for name in pets:
	print(name['owner'] + " has a " + name['kind'])
