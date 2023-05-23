#String formatting in python
'''
String formatting is a method that allows us to embed/combine a string with a non-string. In our case, we're going to
use a string and an integer.
Check the example below...
'''
numbers = [23, 5, 2023] #Here, we define our integers or list in our case.
newstring = "Date:{0}/{1}/{2}".format(numbers[0], numbers[1], numbers[2])
'''In line 8 above, we first define a string we intent to embed with a non string. We declare variable "newstring" and 
pass value "Date" to it. we use the colon, : to specify the numbers we want to merge with the string Date enclosed by 
curly brackets. We then implement the format() function which allows us to perform the string formatting.
In the format function, we then pass the list with their indexes as arguments.
We finally now print the STRING (newstring) we declared, not the LIST (numbers).
'''

print(newstring)


