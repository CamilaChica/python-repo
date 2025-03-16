#For Loops
for item in ['Camila', 'Juan', 'Monica', 'Fabio']:
    print(item)

for item in [1, 2, 3, 4, 5]:
    print(item)

for item in range(10):
    print(item)

for item in range(5, 10):
    print(item)

for item in range(5, 10, 2):
    print(item)

#Excercise
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")

#Nested Loops
#(x, y) - (0, 0) - (0, 1) - (0, 0) - (0, 2)

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

for x in range(3):
    for y in range(4):
        print(f'({x}, {y})')


#Challenge
numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    print('x' * x_count)


numbers = [2, 2, 2, 2, 5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

#Lists
names = ['Camila', 'Juan', 'Monica', 'Fabio']
print(names[0])
print(names[-1])
print(names[2:])
print(names[2:4])
print(names[:])
print(names[2:])
print(names)

names [0] = 'Jon'
print(names[0])


#Excercise
#Write a program to find the largest number in a list.

numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

#2D Lists

# 3x3 - We can model this in Python with a @D List
# A 2D List in Python is a list where each item in that list is another list

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])

# We can modify the items in the list:
matrix[0][1] = 20
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)

#List Methods

numbers = [5, 2, 1, 7, 4]
numbers.append(20) # appends an item in the end of the list
print(numbers)

numbers.insert(0, 13) #inserts  an item in a specific position in the list
print(numbers)

numbers.remove(13)
print(numbers)

numbers.clear()
print(numbers)
#---------------
numbers = [5, 2, 1, 7, 4]
numbers.pop() #remove the last item in the list
print(numbers)

print(numbers.index(5)) #looks up for the existence of an item in the list

print(50 in numbers) #looks up for the existence of an item in the list - it gives a Boolean

numbers = [5, 2, 1, 5, 7, 4]
print(numbers.count(5)) # It tells us how many of the same items are in the list

numbers.sort() #None is an object in python that represents the absense of a value
print(numbers) #The list is sorted in ascending order

numbers.reverse() #None is an object in python that represents the absense of a value
print(numbers) #The list is sorted in descending order

numbers2 = numbers.copy() #It makes a copy of our list
numbers.append(10)
print(numbers2)

#Excercise
# Write a program to remove the duplicates in a list.

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)