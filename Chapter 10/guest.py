prompt = "What's your name? "
user_name = input(prompt)

filename = 'guest.txt'

with open(filename, 'w') as file_object:
	file_object.write(user_name)
