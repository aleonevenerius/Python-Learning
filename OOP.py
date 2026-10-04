
'''
OOP means Object-Oriented Programming and it uses classes and objects for a better orgnazation and reusabilitiy.

Advantages of OPP
* Clean structure to programs
* Makes code easier to maintain, reuse and debug
* Helps keep your code DRY (Don't Repeat Yourself)
* Allows you to build reusable applications with less code

What are Classes and Objects?
Class defines what an objects should look like and an object is created based on that class

EX:
class       object
Fruit       Apple, banana, mago
'''

# Note: everything in python is an object with its properties and method
'''
# Create a Class
class Car:
    motor = "Vrum Vrum!!!!!"
    pass # Class cannot be empty. Nevertheless, you can put into it a pass statement to avoid getting an error.

# Create a Object
car1 = Car()

print(car1.motor)

del car1
Class Person:
    def __init__(self ,name, age, city, country): # Built-in method. It executes whenever an object is used into the class.
        self.name = name
        self.age = age
        self.city = city
        self.country = country
    # Withou it, you would need probably to set the properties manually for each object.      ]]
class Person:
    pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

p1 = Person("Thaly", 18, "New York", "EUA")
print(p1.city)
'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
	    print(self.name + " says Woof!")

d1 = Dog("Buddy", 3)

d1.bark()

# The 'self' parameter is a reference to the current instance of the class. It is used to acess properties and method that belong to the class.
# It must be the first parameter.
# Without it, python would not know which object's properties you want to acess
# 'self' can call whenever you want
# You can acess any property of the class using self.

class Car:
    def __init__(it, model, year, colour):
        it.model = model
        it.year = year
        it.colour = colour
    def ToTalkAboutIt(it):
        print(f"My car is {it.model} release in {it.year}. The colour its is {it.colour}.")

c1 = Car("Hyundai Azera", 2008, "Black")
c1.ToTalkAboutIt()
'''

#                   Class properties
# Properties are variables that belong to a class. They store data for each object created from the class.
class Person:
    specie = "Homo-sapiens" # Class property
    
    def __init__(self, name, age):
        self.name = name # Instance property
        self.age = age


Notes:
* Properties within __init__() belong to each object. It called instace properties.
* Properties outside __main__ and into a class itself is called class properties. Besides, that properties are shared by all objects.


p1 = Person("Lara", 18)
print(p1.name) # using dot to acess object properties
print(p1.age)
# Change property
p1.age = 79
print(p1.age)
del p1.age # Deleting
#print(p1.age) # Error

'''
class Person:
    specie = "Human"

    def __init__(self, name):
        self.name = name

p1 = Person('Lara')
p2 = Person('Alexandre')

print(p1.name)
print(p2.name)
print(p1.specie)
print(p2.specie)

# BE THOUGHTFULL
# When you change a class property you change all object. You should be quite careful

Person.specie = "Golden Monkey"
print(p1.specie)
print(p2.specie)

#                       ADD NEW PROPERTIES
p1.age = 18
p1.city = "Colatina"
p2.age = 19
p2.city = p1.city

print(p1.city)
print(p1.age)
print(p2.city)
print(p2.age)

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s1 = Student("Anna", "A")
print(f"Student: {s1.name}\nGrade: {s1.grade}")
s1.grade = "B"
print(f"Oops... It isn't correct. I apologize. The correct grade is {s1.grade}")
