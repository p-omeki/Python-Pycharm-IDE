#Modules in Python
'''
Modules are pieces of code in python written by other programmers that u can import and use in your code
What I am going to show in this code basically is how you can easily import a module and use it in your code.
'''
import random   #We, initialize the module by importing it.
for x in range(5):

 result = random.randint(1, 6) #We access any function related to the module. In this case ".randint()"
 print(result)