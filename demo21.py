#Lambdas in python
'''
Similar to function but with lambdas, there are some key differences, they don't have a variable name u can pass them
through, and they also don't have a return statement.
To clearly show this, I'll create two example, one of a normal functions and one of a lambdas...
'''
## Finding Square of 4 and 30 in function and lambdas respectively.

#Function
def square(x):
    return x**2
print(square(4))

#Lambdas

print((lambda x: x**2)(30)) #Here, clearly u can see that we've passed our code in a single line. No return statement