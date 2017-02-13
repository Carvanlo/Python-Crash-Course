filename = 'learning_python.txt'

# first version

with open(filename) as file_object:
	contents = file_object.read()
	print(contents)

# second version

with open(filename) as file_object:
	for line in file_object:
			print(line.rstrip())
			
# third version

with open(filename) as file_object:
	lines = file_object.readlines()
	
file_string = ''
for line in lines:
	file_string += line.rstrip()
	
print(file_string)
