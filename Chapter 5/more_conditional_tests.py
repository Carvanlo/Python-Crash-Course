# equality and inequality
phone = 'apple'
print(phone == 'apple')
print(phone != 'apple')

# use lower() function
car = 'BMW'
print(car.lower() == 'bmw')
print(car.lower() == 'BMW')

# numberical tests
age = 18
print(age == 18)
print(age != 18)

print(age > 16)
print(age < 21)

print(age >= 18)
print(age <= 21)

# and keyword and the or keyword
phone = 'samsung'
car = 'audi'

print(phone == 'samsung' and car == 'audi')
print(phone == 'apple' and car == 'audi')
print(phone == 'apple' and car == 'bmw')

print(phone == 'samsung' or car == 'audi')
print(phone == 'apple' or car == 'audi')
print(phone == 'apple' or car == 'bmw')

# whethe in a list
phone = ['samsung', 'apple', 'xiaomi']

print('apple' in phone)
print('htc' in phone)

# whethe not in a list
month = ['Jan', 'Feb', 'Sept']

print('Mar' not in month)
print('Jan' not in month)
