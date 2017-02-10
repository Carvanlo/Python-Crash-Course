current_users = ['melo', 'james', 'cp3', 'dwade', 'admin']
new_users = ['melo', 'admin', 'john', 'fat', 'Bob']

current_users_lower = [users.lower() for users in current_users]

for new_user in new_users:
	if new_user.lower() in current_users_lower:
		print("Sorry " + new_user + ", that name is taken.")
	else:
		print("Great, " + new_user + " is still available.")
