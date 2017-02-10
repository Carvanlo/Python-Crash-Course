favorite_numbers = {
	'melo': [7, 15],
	'james': [23, 6],
	'paul': [3, 15],
	'dwade': [3],
	'yao': [11]
	}

for name, numbers in favorite_numbers.items():
	print("\n" + name + " 's favorite number are:")
	for number in numbers:
		print("\t" + str(number))
