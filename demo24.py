#Generators in Python
'''
Generators are similar to list and tuples but in their case, u can only generate them by using the while loops and the
for loops.
Also, in generators, we don't have a print statement and in it's place we use yield which returns the result...
Check the code below...
'''
#While Loop for Generators
def gfunctions(): #We define an empty function "gfunctions()"
    counter = 0
    while counter < 5:
        yield counter
        counter += 1
for x in gfunctions():
    print(x)
#Using Generators to create a list of even numbers
def gfunctions(x):
    for i in range(x):
        if i % 2 == 0:
            yield i
print(list(gfunctions(21)))
