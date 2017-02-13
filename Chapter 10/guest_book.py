prompt = "What's your name? "
filename = 'guest_book.txt'

print("(Enter 'q' if you want to exit.)\n")

while True:
	user_name = input(prompt)
	if user_name == 'q':
		break
	else:
		with open(filename, 'a') as file_object:
			file_object.write(user_name + "\n")
