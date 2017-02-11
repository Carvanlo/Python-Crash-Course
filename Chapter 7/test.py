prompt = "Please enter your age and I will tell you the ticket price."
prompt += "\n(You can enter 'quit' to quit the system.) "

while True:
	age = input(prompt)
	if age == 'quit':
		break
	elif int(age) < 3:
		print("You are free for the ticket.")
	elif int(age) < 12:
		print("The ticket is $10.")
	elif int(age) >= 12:
		print("The ticket is $15.")
