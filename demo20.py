#Functional programming in Python
'''
Functional Programming is a style of programming that involves using functions to write code.
It's useful if a function in a given programming language has two abilities:
      1.To take another function as an argument
      2.To return another function to its caller
'''
def inner(): #Here, we've defined function inner()
   print("I am function inner()!")
def outer(function): #Defined function outer()
   function()

outer(inner) #We've passed function inner() as a parameter of function outer() by calling outer() function