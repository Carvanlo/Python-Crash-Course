guest_list = ['fat', 'melo', 'james']

# I find a big table, so i can invite more peoples.
guest_list.insert(0, 'howard')
guest_list.insert(2, 'Curry')
guest_list.append( 'yao')

# print the inviting messages
invite = '. Would you like to have dinner with me?'
message0 = 'Hi, ' + guest_list[0] + invite
message1 = 'Hi, ' + guest_list[1] + invite
message2 = 'Hi, ' + guest_list[2] + invite
message3 = 'Hi, ' + guest_list[3] + invite
message4 = 'Hi, ' + guest_list[4] + invite
message5 = 'Hi, ' + guest_list[5] + invite

print(message0)
print(message1)
print(message2)
print(message3)
print(message4)
print(message5)

# I find out my new dinner won't arrive in time,
# so i can just invite two guests

uninvited_guest = guest_list.pop()
message = "sorry, " +uninvited_guest + ". i can't have dinner with you."
print(message)

uninvited_guest = guest_list.pop()
message = "sorry, " +uninvited_guest + ". i can't have dinner with you."
print(message)

uninvited_guest = guest_list.pop()
message = "sorry, " +uninvited_guest + ". i can't have dinner with you."
print(message)

uninvited_guest = guest_list.pop()
message = "sorry, " +uninvited_guest + ". i can't have dinner with you."
print(message)

# send message to the person still on my list
invite = '. Would you like to have dinner with me?'
message0 = 'Hi, ' + guest_list[0] + invite
message1 = 'Hi, ' + guest_list[1] + invite

print(message0)
print(message1)

