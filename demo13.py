#Errors and Exceptions in Python
'''
Errors are majorly caused by lack of properly following programming rules and regulation when writing your lines of code
In this demo, I'll focus on two major types of errors, that is the Syntax error and the Logical error.
Syntax error is mostly caused by missing out essential syntax in the code necessary to run it.
Logical error, first it's difficult to be noticed by the compiler as it will give an output regardless unlike in Syntax
error.
Check the example below...
'''

# 1. Normal function call
def add(a, b):  #Now, this code has the perfect syntax and if we remove the  colon (:) after defining the function
                   #  ...it will give a syntax error
    print(a+b)   #Now, on the logical error, in this line 14 we've clearly defined an addition of a and b but we may change
                   #... it to * or / and it will still give us an answear, but logically we wanted an addition of a and b
                   #...In this case, we'll get a logical error.

add(2, 3)

'''Let's talk Exceptions, this are basically code terminators that ends our code and prevent further execution. Now, as 
programmers, it's important that one learn how to handle exceptions which I'll talk about in demo13.1.py.
'''