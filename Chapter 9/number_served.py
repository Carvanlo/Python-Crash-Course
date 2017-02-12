class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
		
	def describe_restaurant(self):
		print(self.restaurant_name.title())
		print(self.cuisine_type)
		
	def open_restaurant(self):
		print(self.restaurant_name.title() + " is open.")

	def set_number_served(self, number):
		self.number_served = number

	def increment_number_served(self, number):
		self.number_served += number

restaurant = Restaurant('tang', 'chinese')
print(restaurant.number_served)

restaurant.set_number_served(3)
print(restaurant.number_served)

restaurant.increment_number_served(20)
print(restaurant.number_served)
