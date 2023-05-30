#Inheritance in Python
'''
Inheritance in python, well, in simple terms of what inheritance means is that a child inheritance assets from the
parent. Now, in python, Inheritance works in the same similar manner, the only difference here is inheritance is among
class.
Check the example below...
'''
#Creating a class of Students
class Students:   #The student will act as the parent class

#We define the class attributes/properties
    def __int__(self, Name, Contact): #The __init__() is a method used as a contructor for initializing the objects of
                                           # a class and the self is a reference to the object being created.
        self.Name = Name
        self.Contact = Contact

#We define the class methods
    def LoginData(self):
        print("Enter your credentials")
        self.Name = input("Enter name: ")   #The methods name can be any name...We've used LoginData() & DisplayData
        self.Contact = input("Enter contact: ")
    def DisplayData(self):
        print("Name is: "+self.Name)
        print("Contact is: "+self.Contact)

class ScienceStudent(Students): #The ScienceStudent is the child of Students and we've passed parent as an argument in that case.

    #We define the attributes of ScienceStudents
    def __int__(self, age):
        print("Am a science student of class Students")
        self.age = age

    #We define ScienceStudents method

    def YourAge(self):
        print("Hey, this is my age")
        self.age = input("Enter age: ")

    #We define the object ~ in our case we'll use "Patrick"

Patrick = ScienceStudent()
Patrick.YourAge()
Patrick.LoginData() #We've passed Parents methods onto the Child ~ Inheritance...right there mate.
Patrick.DisplayData()
