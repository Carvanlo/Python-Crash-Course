rivers = {'nile' : 'egypt', 'Changjiang': 'china', 'amazon': 'brazil'}

for river, country in rivers.items():
	print("The " + river + " runs through " + country)
	
print("\nHere is the river name:")
for river in rivers.keys():
	print(river)
	
print("\nHere is the country name:")
for country in rivers.values():
	print(country)
