filename = 'learning_python.txt'

with open(filename) as file_object:
	lines = file_object.readlines()
	
file_string = ''
for line in lines:
	file_string += line.rstrip()

file_string.replace('python', 'c')
print(file_string)
