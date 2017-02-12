class Restaurant():
	def __init__(self, name, cuisine_type):
		self.name = name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		print(self.name.title())
		print(self.cuisine_type)
		
	def open_restaurant(self):
		print(self.name.title() + " is open.")

class IceCreamStand(Restaurant):
	def __init__(self, name, cuisine_type='ice_cream'):
		super().__init__(name, cuisine_type)
		self.flavors = []
		
	def display_flavors(self):
		print("We have the following flavors:")
		for flavor in self.flavors:
			print("-" + flavor)
			
ice_cream_stand = IceCreamStand('Lucky')
ice_cream_stand.flavors = ['vanilla', 'chocolate', 'black cherry']
ice_cream_stand.display_flavors()
