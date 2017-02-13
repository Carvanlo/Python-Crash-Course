def print_file(filename):
	try:		
		with open(filename) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		print("The file " + filename + " is missing.")
	else:
		print(contents)
			
filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
	print_file(filename)
