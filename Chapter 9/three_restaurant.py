class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		print(self.restaurant_name.title())
		print(self.cuisine_type)
		
	def open_restaurant(self):
		print(self.restaurant_name.title() + " is open.")

restaurant_1 = Restaurant('tang', 'chinese')
restaurant_2 = Restaurant('love', 'Italy')
restaurant_3 = Restaurant('pairs', 'French')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
