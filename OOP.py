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

