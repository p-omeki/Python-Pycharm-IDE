#Operator Overloading In Python
'''
Operator overloading is a method that allows us to perform an operation on a code, either addition,subtraction,
 multiplication, division, modulo, greater than, less than, e.t.c by
 overloading an operator, +/- . Now, a normal add or sub operation we'll declare the operation and run the code, here
the +/- result is given based on the particular function definition we've defined and so, we decide what the operator
will do, not just add automatically.
In summary, it allows a programmer to define the behaviour of an operator when applied to a user-defined objects or
classes.
Check the code below...
'''
#Performing an operator overloading to calculate two coordinates
class Points:
    def __init__(self, x, y):   #We define the class for our operator overloading and pass two cordinates
        self.x = x
        self.y = y

    def __add__(self, other):   #Overloads the addition operator for Points class
        x = self.x + other.x
        y = self.y + other.y
        return Points(x, y)

    def __str__(self):  #Overloads the string representation of the object (str() or print()
        return "({},{})".format(self.x, self.y)

point1 = Points(1, 2)   #Defining the object of class...
point2 = Points(2, 4)
Result = point1 + point2 # '+' operator is overloaded for coordinates x and y

print(Result)