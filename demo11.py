#Passing fuctions as arguments

def add(a, b):  #We first define the function
    return a + b   #Notice, we'll not introduce the third variable c and instead return the addition directly.

def square(c):   #We define our second function that will call our first function into.
    return c * c   #Returns the square of

result = square(add(2,3))
'''Now, in the above line, we call the function square by defining it in a variable result which will output the square.
So, how have we passed the function? Notice we've passed the add() function inside the square() function. What this will
do is that it will first call the add() function and execute the arguments inside add() function that's 2 and 3 giving 
5 and now the sqaure function will have an argument 5, represented as c and after finding it square, an output of 25.
We therefore, would have passed the function as argument.
'''
print(result)