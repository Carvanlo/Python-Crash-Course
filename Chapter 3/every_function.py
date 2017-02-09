guest_list = ['fat', 'melo', 'james']

print(guest_list[1])

print(guest_list[-1])

guest_list.append('cp3')
print(guest_list)

del guest_list[0]
print(guest_list)

delete = guest_list.pop(0)
print(delete)

guest_list.remove('james')
print(guest_list)

guest_list.insert(0, 'howard')
guest_list.insert(1, 'yao')
guest_list.insert(2, 'rose')
print(guest_list)

print('\nSorted list')
print(sorted(guest_list))

guest_list.sort()
print(guest_list)

print('Reversed:')
guest_list.reverse()
print(guest_list)
