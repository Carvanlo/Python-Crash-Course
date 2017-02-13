prompt = "\nWhy do you like programming? "
filename = 'programming_poll.txt'

print("(Enter 'q' if you want to exit.)")

while True:
	reason = input(prompt)
	if reason == 'q':
		break
	else:
		with open(filename, 'a') as file_object:
			file_object.write(reason + "\n")
			print("Your reason has been added to our file.")
