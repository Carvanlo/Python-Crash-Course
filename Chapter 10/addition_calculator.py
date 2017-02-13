print("Give me two numbers, and I'ill add them.")
print("Enter 'q' to exit.")

while True:
	try:
		first_number = input("\nFist_number: ")
		if first_number == 'q':
			break
		x = int(first_number)	
			
		second_number = input("Second_number: ")
		if second_number == 'q':
			break
		y = int(second_number)	
	
	except ValueError:
		print("You should input a number!.")
	else:
		answer = x + y
		print("The sum of " + str(x) + " and " + str(y) + " is " + str(answer) + ".")
