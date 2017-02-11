prompt = "Please enter the topping you want to add to your pizza."
topping = ""

while topping != 'quit':
	topping = input(prompt)
	if topping != 'quit':
		print("I will add " + topping + " to your pizza.")
