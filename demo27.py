#Recursion in Python
'''
Recursion is python means, a function calling itself within the function definition. For us to understand better, we
answear this question. How do we call a function? We call a function by first defining the function and calling the
function outside the function definition. Now, in Recursion, the function is called withing the function definition.

Check the example below where we'll use recursion to get factorial of a number...
'''
#Getting factorial of 5 using recursion
def fiveFactorial(x):
    if (x == 1):  #We give a condition for the recursion to continue with the iteration
        return 1
    else:
        return x*fiveFactorial(x-1) #We define the factorial formula

Result = fiveFactorial(5)
print(Result)