# Object Oriented Programing (OOP)
# It is a programming concept (paradigm) that describes how to think and organize code. This one specifies that everything is an object.
# It defines how to structure and organize code in a way that is easy to understand and maintain.

# Has to core concepts Classes and Objects
# Class is a blueprint or template for creating objects. It defines the properties and behaviors that objects of that class will have.
# Object is an instance of a class. It is a concrete representation of the class with its own unique state and behavior.

# For example, a class can represent a notebook, with properties like color, make and model. And a concrete object is mine or yours notebook.


# Class
# Basic structure: class keyword name of class (classes are always capitalized):
class EmptyNotebook:
    pass  # used to create a class without any properties or methods


# Object
# Basic structure: variable name = class name()
# From one class we can create multiple objects
my_empty_notebook = EmptyNotebook()  # creating / instantiating the object
your_empty_notebook = EmptyNotebook()


# Classes can contain properties and methods
# Class property is like a variable belonging to the class or object
# Class method are functions belonging to the class
# Most classes have constructors to initialize object properties


class Notebook:
    # this is property of the class, and it is the same for all objects constructed from this class
    description = "A notebook is a portable writing surface with a cover and pages for recording notes, writing, or drawing."

    # constructor of class
    # special method which is called when the object is created
    def __init__(self, manufacturer, color="black"):

        # these are properties of the object
        self.manufacturer = manufacturer
        self.color = color

    # the first param of any method is self - self represents the current object (instance of the class)
    def describe(self):

        # through self any property or method of the class can be accessed
        print("You are looking at notebook:")
        print(self.color)
        print(self.manufacturer)


my_asus_notebook = Notebook("Asus")  # arguments are passed to constructor
print(my_asus_notebook.manufacturer)  # accessing color property of an object
my_asus_notebook.color = "red"
my_asus_notebook.describe()  # calling describe method of an object
print(my_asus_notebook.description)

my_dell_notebook = Notebook("Dell")
print(my_dell_notebook.manufacturer)
my_dell_notebook.color = "blue"
my_dell_notebook.describe()
print(my_dell_notebook.description)

# Changing class property will change it for all of them
Notebook.description = "A notebook everybody knows what it is..."

print("Asus description:", my_asus_notebook.description)
print("Dell description:", my_dell_notebook.description)

# Inheritance allows defining child classes which will inherit all the properties and methods from the parent (base) class
# This allows reusability of code and easier structuring


class GamingNotebook(Notebook):

    # this function is overriding the parent class method; in case we want to pass data down to parent (which we always want), we need to call parents __init__ method
    def __init__(self, manufacturer, boost_length, color="black"):
        # for that we can use super() method which means parent object
        super().__init__(manufacturer, color)
        self.boost_length = boost_length

    def boost(self):
        print(f"Boosting performance...for {self.boost_length} seconds")


print("Example: Inheritance - Creating Gaming Notebook")
my_gaming_notebook = GamingNotebook("MSI", boost_length=5)
my_gaming_notebook.describe()  # this method exists in Notebook class (parent)
my_gaming_notebook.boost()  # this method is specific to the GamingNotebook class

# Polymorphism means "many forms" and describes a concept that methods/functions/operators with the same name can be executed on many objects or classes.
# For example function len() is able to show length of multiple collections (string, list, tuple)

# For classes, we can use polymorphism in combination with inheritance to achieve code reuse and flexibility. By defining methods with the same name in different classes, we can write generic code that works with objects of various types.


class Vehicle:
    pass


class Car(Vehicle):

    def honk(self):
        print("Car goes: Tuu! Tuu!")


class Bicycle(Vehicle):
    def honk(self):
        print("Bicycle goes: Cr! Cr!")


class ContainerBoat(Vehicle):
    def honk(self):
        print("Container boat goes: Tuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu!")


print("Example: Polymorphism - Honking of different vehicles")
car = Car()
bicycle = Bicycle()
boat = ContainerBoat()

car.honk()
bicycle.honk()
boat.honk()


# Encapsulation is the practice of hiding the internal details of an object and exposing only the necessary information to the outside world. This helps to prevent unintended modifications and ensures that the object's behavior remains consistent.
# Python does not have a built-in mechanism for encapsulation like some other languages, but it can be achieved through naming conventions - properties and methods starting with a single underscore (_) are considered private and should not be accessed directly.
class Hero:
    def __init__(self, name, real_identity):
        self.name = name
        self._real_identity = real_identity


print("Example: Encapsulation - Creating hero profiles")
batman = Hero("Batman", "Bruce Wayne")
print(batman.name)
# Note IDE should show a warning regarding access to private property
print(batman._real_identity)
