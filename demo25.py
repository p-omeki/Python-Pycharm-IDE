#Object oriented programming in python
'''
OOP as the name suggest is about objects, the creation of objects and usage of objects as instance of a class. And what
is a class? It's a blueprint for creating objects. So, for an object to exist, there must be a class.
In OOP, there are 4 major aspects we'll look up to in depth, these are: A class, an attribute/properties, a method and lastly
object. Clearly, when it comes to object-oriented programing, we define our code in that order...
Class->Attribute->Method->Object. The attribute is now the variable stored in an instance or class or in a layman's
language, it describes the class. The method is a function stored in an instance or class, and it's used to define what
the class does or what we need the class to do. We "define" methods in OOP.

Let's now dive deeper in OOP with the example below...
'''
#Creating a class of Students
class Students:

#We define the class attributes/properties
    def __int__(self, Name, Contact):
        self.Name = Name
        self.Contact = Contact

#We define the class methods
    def LoginData(self):
        print("Enter your credentials")
        self.Name = input("Enter name: ")
        self.Contact = input("Enter contact: ")
    def DisplayData(self):
        print("Name is: "+self.Name)
        print("Contact is: "+self.Contact)

#We define the objects of the class. In our case we'll use 'KeyIn'
KeyIn = Students()
KeyIn.LoginData()
KeyIn.DisplayData()
