places = ['Guangzhou', 'Shenzhen', 'Shanghai', 'Beijing', 'Houston']
print(places)

print('\nHere is the sorted list.')
print(sorted(places))

print('\nHere is the original list again.')
print(places)

print('\nHere is the sorted list in reverse.')
print(sorted(places, reverse = True))

print('\nHere is the original list again.')
print(places)

print('\nHere is the reversed list.')
places.reverse()

print(places)

print('\nHere is the original list.')
places.reverse()
print(places)

print('\nHere is the sorted list.')
places.sort()
print(places)

print('\nReversed:')
places.sort(reverse = True)
print(places)
