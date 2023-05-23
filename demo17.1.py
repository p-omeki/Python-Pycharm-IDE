#List Comprehension in Python
'''
List comprehension is somewhat creation of list automatically after defining a set of rules or condition to be
considered when we'll be creating that list.
E.g We are going to create a list of squares from 0 to 10 and in that also, add "if" statement to printout
only numbers that even and exclude the odd numbers.
'''
#Finding squares of numbers from 0-10

numbers = [x**2 for x in range(11) if x**2 % 2 == 0]
#The above line, we've define the rules for our list that we want printed using the for loop and if statement.

print(numbers)