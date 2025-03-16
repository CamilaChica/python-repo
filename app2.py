#If Statements
is_hot = True
is_cold = False


if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
#Press Shift + Tab to brake the code line, to end the code. / Remove indentation
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")

print("Enjoy your day")

#Excercise

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")

#Logical Operators:

# AND: both conditions should be True
# OR: at least one of the conditions must be True
# NOT:
has_good_income = True

if has_good_income and has_good_credit:
    print("Eligible for loan")

has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for a loan")

#Comparison Operators
# >
# <
# <=
# >=
# ==
# !=

temperature = 30

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

#Exercise

name = "J"
if len(name) < 3:
    print("NAme must be at least 3 characters.")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters.")
else:
    print("Name looks good!")

#Project:
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos.")
else:
    converted = weight /0.45
    print(f"You are {converted} pounds.")

#While loops

i = 1
#while condition:
while i<= 5:
    print('*' *i)
    i = i + 1
print("Done")

#Guessing Game
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print('Sorry :( you failed.')

#Car Game
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that")

