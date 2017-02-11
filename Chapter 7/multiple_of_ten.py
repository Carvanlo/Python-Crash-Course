message = "Please enter a number."
message += "\nI will you whether it is a multiple of 10 or not."
number = input(message)
number = int(number)

if number % 10 == 0:
	print(str(number) + " is a multiple of 10.")
else:
	print(str(number) + " is not a multiple of 10.")
