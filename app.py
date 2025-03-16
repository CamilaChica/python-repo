import math

# Basics
print('Camila Chica')
print('o----')
print(' ||||')
print('*' * 10)


# Variables
#int:
price = 10
price = 20
# float:
rating = 4.9
# string:
name = 'Camila'
# boolean:
is_published = False
print(price)

#Excercise:
#We check in a patient named John Smith. He's 20 years old and is a new patient.

full_name = 'John Smith'
age = 20
is_new = True

#Getting input
##name = input('What is your name? ')
##print('Hi ' + name)

#Excercise
#Ask two questions: person's name and favorite color. Then, print a messae like "Camila likes Blue"
##persons_name = input('I am sorry, I did not get that. What is your name again please? ')
##print('Nice to meet you ' + persons_name)
##favorite_color = input('What is your favorite color? ')
##print('Hmmm I see that ' + persons_name + ' likes ' + favorite_color )

#Type Conversation
##birth_year = input('''Let me know more about you...
##What is your Birth-year: ''')
##print(type(age))

int()
float()
bool()
##age = 2025 - int(birth_year)
##print(type(age))
##print(age)
##age_out = str(age)

#Exercise
#Ask a user their weight (in pounds), convert it to kilograms and print it on the terminal.

##print(age_out)
##print('So, I am getting that your name is ' + persons_name + ', your favorite color is ' + favorite_color + ' and you are ' + age_out)
##print('''years old.
##I'm going to make you a more difficult question, since,
##they've told me that you've been eating a lot of picanha burguer lately
##at Fogo de Chao. ''')
##weight_lbs = input('What is your weight (in pounds)? Do not lie to me -_- ')
##weight_kg = float(weight_lbs) * 0.45
##weight_out = str(weight_kg)

##print('So, you are ' + weight_out + ' Kg. You are full of love!')

#Strings
course = 'Pyton for Beginners'
another = course[:]
print(course[1])
print(course[-2])
print(course[0:3])
print(course[0:])
print(course[:5])
print(another)

#Excercise
name = 'Jennifer'
print(name[1:-1])

#Formated Strings

first = 'John'
last = 'Smith'
message = first + (' [' + last + '] is a coder.')
print(message)
msg = f'{first} [{last}] is a coder.'
print(msg)

#String Methods
course = 'Python for Beginners'
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('P')) #Sensitive case
print(course.find('Beginners'))
print(course.replace('Beginners', 'Absolute Begginers'))
print(course.replace('P', 'J'))

#Boolean

print('Python' in course) #Case sensitive
print('python' in course) #Case sensitive, Returns False

#Arithmetic Operations
print(10+3)
print(10*3)
print(10/3)
print(10//3)
print(10%3)
print(10**3)

x = 10
x= x + 3
print(x)
x+= 3
print(x)
x-= 3
print(x)

#Operator Procedence
# exponentiation 2 ** 3
# multiplication or division
# addition or substraction

x = 10 + 3 * 2
print(x)

x = 10 + 3 * 2 ** 2
print(x)

#parenthesis: always takes priorities
x = (10 + 3) * 2 ** 2
print(x)

x = (2 + 3) * 10 - 3
print(x)

#Math Functions
x = 2.9
print(round(x))
print(abs(-2.9))

#Add "import math" library
print(math.ceil(2.9))
print(math.floor(2.9))

#Open Python math 3 in the Browser

#If Statements




