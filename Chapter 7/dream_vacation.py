response = {}
polling_active = True
name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would you go? "
continue_prompt = "\nWould you like to let someone else respond?(yes/no) "

# Responses will be stored in the form(name: place).
while polling_active:
	name = input(name_prompt)
	place = input(place_prompt)
	
	response[name] = place
	
	repeat = input(continue_prompt)
	if repeat == "no":
		polling_active = False
		
print("\n")
for name, place in response.items():
	print(name + " want to visit " + place + ".")
