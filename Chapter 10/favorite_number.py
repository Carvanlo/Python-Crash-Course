# first program

import json

filename = 'favorite_number.json'
prompt = "What's your favorite number?"
favorite_number = input(prompt)

with open(filename, 'w') as file_object:
	json.dump(favorite_number, file_object)
	
# second program

with open(filename) as file_object:
	favorite_num = json.load(file_object)
print("I know your favorite number! It's " + favorite_num + ".")

