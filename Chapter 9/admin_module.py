from user_module import User
from privileges_module import Privileges

class Admin(User):
	def __init__(self, first_name, last_name,
				username, email, location):
		super().__init__(first_name, last_name,
				username, email, location)
		self.privileges = Privileges()
			
