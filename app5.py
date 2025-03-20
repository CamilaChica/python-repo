#Constructors
from filecmp import DEFAULT_IGNORES


class Point:
   # def __init__(self): # We just added two extra parameters a constructor.
    def __init__(self, x, y): #We just added parameters to our Constructor
        self.x = x #Object is created
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point = Point(10, 20) #'10' and '20' Arguments are going to be passed to 'x' and 'y' Parameters to use them to initialize our Object
print(point.x)

#Excercise
class Person:
    def __init__(self, name): #'self' references the current Object
        self.name = name #We're setting the name Atribute of the current Object to the 'name' Argument passed to this 'name' Method
    def talk(self):
        #print("talk")
        print(f"Hi, I'm John {self.name}")

#john = Person()
#john.talk()
john = Person("John Smith")
#print(john.name)
john.talk()

bob = Person("Bob Smith")
bob.talk()

#Inheritance
class Mammal:
    def walk(self):
        print("walk")
class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")

dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.be_annoying()
cat1.walk()

#Modules

