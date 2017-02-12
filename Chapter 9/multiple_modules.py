from user_module import User
from privileges_module import Privileges
from admin_module import Admin

Eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alask')
Eric.privileges.privileges = ["can add post", "can delete post", "can ban user"]
Eric.privileges.show_privileges()
