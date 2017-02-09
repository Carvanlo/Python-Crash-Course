my_pizzas = ['a', 'b', 'c']
friend_pizzas = my_pizzas[:]

my_pizzas.append('d')
friend_pizzas.append('e')

print("My favorite pizzas are:")
for x in my_pizzas:
	print(x)
	
print("\nMy friend's favorite pizzas are:")
for x in friend_pizzas:
	print(x)
