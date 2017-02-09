guest_list = ['fat', 'melo', 'james']
cannot_come = 'fat'
new_invite = 'cp3'

guest_list.remove(cannot_come)
guest_list.append(new_invite)

invite = '. Would you like to have dinner with me?'
message1 = 'Hi, ' + guest_list[0] + invite
message2 = 'Hi, ' + guest_list[1] + invite
message3 = 'Hi, ' + guest_list[2] + invite

print(message1)
print(message2)
print(message3)

