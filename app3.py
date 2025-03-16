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

