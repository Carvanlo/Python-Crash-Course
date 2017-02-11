# Exercise 7-4

# conditional test

prompt = "Please enter the topping you want to add to your pizza. "
topping = ""

while topping != 'quit':
	topping = input(prompt)
	if topping != 'quit':
		print("I will add " + topping + " to your pizza.")

# active variable

prompt = "Please enter the topping you want to add to your pizza. "

active = True

while active:
	topping = input(prompt)
	if topping == 'quit':
		active = False
	else:
		print("I will add " + topping + " to your pizza.")
		

# break statement

prompt = "Please enter the topping you want to add to your pizza. "

while True:
	topping = input(prompt)
	if topping == 'quit':
		break
	else:
		print("I will add " + topping + " to your pizza.")


# Exercise 7-5

# conditional test

prompt = "Please enter your age and I will tell you the ticket price."
prompt += "\n(You can enter 'quit' to quit the system.) "
age = ""

while age != 'quit':
	age = input(prompt)
	if age != 'quit':
		if int(age) < 3:
			print("You are free for the ticket.")
		elif int(age) < 12:
			print("The ticket is $10.")
		elif int(age) >= 12:
			print("The ticket is $15.")
	
	
# active variable

prompt = "Please enter your age and I will tell you the ticket price."
prompt += "\n(You can enter 'quit' to quit the system.) "

active = True

while active:
	age = input(prompt)
	if age == 'quit':
		active = False
	elif int(age) < 3:
		print("You are free for the ticket.")
	elif int(age) < 12:
		print("The ticket is $10.")
	elif int(age) >= 12:
		print("The ticket is $15.")

# break statement

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

