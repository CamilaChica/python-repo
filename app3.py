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
