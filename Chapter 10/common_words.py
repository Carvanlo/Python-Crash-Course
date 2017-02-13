filenames = ['the_medieval_latin_hymn.txt',
			'dorothy_dale_and_her_chums.txt']

for filename in filenames:
	with open(filename) as file_object:
		contents = file_object.read()
		number = contents.lower().count('the')
		print(number)
