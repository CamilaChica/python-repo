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

