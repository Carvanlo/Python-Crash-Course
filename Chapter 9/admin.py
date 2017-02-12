class User():
	def __init__(self, first_name, last_name, username, email, location):
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.email = email
		self.location = location.title()
		
	def describe_user(self):
		print("\n" + self.first_name + " " + self.last_name)
		print(" Username: " + self.username)
		print(" Email: " + self.email)
		print(" Location: " + self.location)
		
		
	def greet_user(self):
		print("\nWelcome back, " + self.username + "!")

class Admin(User):
	def __init__(self, first_name, last_name,
				username, email, location):
		super().__init__(first_name, last_name,
				username, email, location)
		self.privileges = []
		
	def show_privileges(self):
		print("The following is your privileges:")
		for privilege in self.privileges:
			print("-" + privilege)
			
Eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alask')
Eric.privileges = ["can add post", "can delete post", "can ban user"]
Eric.show_privileges()
