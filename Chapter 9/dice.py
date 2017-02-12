from random import randint

class Die():
	def __init__(self, sides):
		self.sides = sides
		
	def roll_die(self):
		x = randint(1, self.sides)
		print(x)
		
sided_6 = Die(6)
print("Make a 6-sided die and roll it 10 times.")
for roll_num in range(10):
	sided_6.roll_die()
	

sided_10 = Die(10)
print("\nMake a 10-sided die and roll it 10 times.")
for roll_num in range(10):
	sided_10.roll_die()
	

sided_20 = Die(20)
print("\nMake a 20-sided die and roll it 10 times.")
for roll_num in range(10):
	sided_20.roll_die()
