print("Hello world")
msg = "Hello World"
# Concatenation

firstname = 'albert'
lastname  = 'einstein'

fullname = firstname + ' ' +lastname
print(fullname)

#lists
bikes = ['trek','redline','giant']
first_bike = bikes[0]
last_bike = bikes [-1]
print(first_bike, last_bike)

for bike in bikes:
    print(bike, end = ' ')

bikes = []
bikes.append('trek')
bikes.append('redline')
bikes.append('giant')
print(bikes,end = ' ')
print(" ")
square = []
for x in range(1,11):
    square.append(x**2)
print(square)

# List comperhensions
squares = [x**2 for x in range(1,11)]
# Slicing a list
finishers = ['sam', 'bob','ada','bea']
first_two = finishers[:2]
print(finishers)
print(first_two)
# Copy a list
copy_of_bikes = bikes[:]
print(copy_of_bikes)

# Tuples
dimensions = (1920, 1080)

# If statements
# Conditional test with lists

boolA = 'trek' in bikes
print(boolA)
print('surly' not in bikes)

# Dictionaries
alien = {'color': 'green', 'points': 5}
print("The alien's color is = "+ alien['color'])
alien['x_position'] = 0
print(alien)

# Looping through all key-value paris
fav_numbers = {'eric': 17, 'eve':4}
for name, number in fav_numbers.items():
    print(name, number)

for name in fav_numbers.keys():
    print(name + ' Loves a number ')

for name in fav_numbers.values():
    print(str(number) + ' is a favorite')


# User Inputs
#name = input ("what's your name")
#print("Hello, " + name + "!")

# While loops

current_value = 1
while current_value <= 5:
    print(current_value)
    current_value +=1

# msg = ''
# while msg != 'quit':
#     msg = input("What's your message")
#     print(msg)

# Functions

def greet_user():
    """ Display a simple greeting. """
    print("Hello")

# Catching an exception
# prompt = 'How many tickets do you need:'
# num_tickets = input(prompt)

# try:
#     num_tickets = int(num_tickets)
# except ValueError:
#     print("Please try again.")
# else:
#     print("Your tickets are printing.")

# Lists
users = ['val','bob','mia','ron','ned']

first_user = users[0]
second_user = users[1]
newest_user = users[-1]

# insert an element at particular position

users.insert(3,'ghasak')
print(users)

