#Understanding for loops in Python
'''
For loops is used when u want to run a program multiple number of times. Uses what's called an interation and what that
does is that it when u defined a for loop and let's say u give it variable "x" and startup to be 0, and an interval of
let's say 11, what it will do is that it will first assign 1 to x on first loop, then assign 2 to x on the second loop
or interation.
Check the below example:
'''
for x in range(1,11): #We've decalred the starting point to be 1 and intervals max to be 11

    print (x) #This will print number from 1 to 10

#Using for loop to print out a list

fruits = ["Mango", "Banana", "Oranges", "Avocado", "Apple"]

for x in fruits:  #Here, u can either specify the range or the list
    print(x)