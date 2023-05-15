#This is an if statement in Python
'''
If statement are used to print a condition found to be true and if not returns no output. And, so, in this code, we're going
to code a simple if statement to determine whether an person is an adult or not
'''

age = input("Enter your age: ")
#Rem: The values will put will be displayed as a string and so we change it to an interger below.

age = int(age)
'''How do we prevent ourselves from repeating the same variale in the line above when converting to an interger?
Well, we'll declare the input() inside the int().
Like this, age = int(input("Enter your age: ")) ~ We'll use this format from here onwards.
'''

if age >= 18:
    print("You're an adult")
else:
    print("You're not an adult")