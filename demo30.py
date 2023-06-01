#Operator Overloading In Python
'''
Operator overloading is a method that allows us to perform an operation on a code, either addition or subtraction by
overloading an operator, +/- . Now, a normal add or sub operation we'll declare the operation and run the code, here
the +/- result is given based on the particular function definition we've defined and so, we decide what the operator
will do, not just add automatically.
In summary, it allows one operator to be used with different meaning.
Check the code below..
'''
#Performing an operator overloading to calculate two coordinates
class Points:
    def __init__(self, x, y):   #We define the class for our operator overloading
        self.x = x
        self.y = y

    def __add__(self, other):   #We define the add operator for our overloading
        x = self.x + other.x
        y = self.y + other.y
       # return Points(x, y)
'''
    def __str__(self):
        return "({0},{1})".format(self.x, self.y)
'''
point1 = Points(1, 4)
point2 = Points(2, 8)
print(point1 + point2)