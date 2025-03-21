#Keyword Arguments
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard.')


print("Starts")
greet_user(last_name="Smith", first_name="John" ) #When we supply a keyword argument, the position doesn't really matter.
print("Finish")

#Most of the time we use positional arguments, but these keyword arguments will help us to improve the readability of our code.
#When we use numerical arguments, it's a better practice to include keyword arguments to improve the readability of our code.
#Example: #calc_cost(total=50, shipping=5, discount=0.1)
#If we try to mix keyword argument and positional argument, it would give us an error. If necessarily needed, we can write the positional argument first and then the keyword argument.
#example: greet_user("John", last_name="Smith" )

#Return Statement
#Functions that return values
def square(number):
    return number * number
result = square(3)
print(result)


#Simplier:
def square(number):
    return number * number
print(square(3))


#This gets None. 'None' is the absence of a value, it happens because we need to include 'return'.
def square(number):
    print(number * number)
print(square(3))

#Creating a Reusable Function
# Emoji Converter :)
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "🙂",
        ":(": "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input("> ")
print(emoji_converter(message))


#Exceptions
#An exception is a kind of error that crashes our programm.
#age = int(input('Age: '))
#print(age)
#If the user inputs a value different than an int. It gives us a ValueError. Exit code will not be '0'.
#How to handle it:
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid Value')

#Comments

#This is a comment and it should be used to explain: (Why - How)
print("Sky is blue")

#Classes
# We can use classes to define new types to model real concepts.
# NAme convention: CamilaChica (Capitalize each word)
class Point: #We just defined a new type
    def move(self):
        print("move")
    def draw(self):
        print("draw")

#Objects
#Instance of a class
point1 = Point() #We store the object in a variable
point1.x = 10 #We give an attribute that we can set anywhere in our programs
point1.y = 20
point1.draw()  #Draw Method is printed in the terminal. When we use the '. operator' we can use the methods that we previously defined and many others.

#Let's create another object. Each object is an instance of a Class
point2 = Point()
point2.x = 1
print(point2.x)





