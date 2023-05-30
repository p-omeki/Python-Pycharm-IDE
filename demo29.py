#Itertools in python
'''
Itertools are modules used as tools in functional programming. Since they're modules, for us to use them we simply have
to import them to our code. Itertools have different function used with it, but on this article we are going to focus
on three functions that are mostly used. This includes:
       1.The count ~ The function iterates a number to infinite once the start is specified.
       2.The accumulate ~ The function adds the corresponding
       3.The takewhile ~ The function takes an element from a list while a certain condition is TRUE.

'''
#Count function
'''from itertools import count    #This line states, from module itertools, import function count...

for i in count(3):
    if i > 20:
        break
    print(i) #This will print to infinite, so we set a condition to break when it reaches a certain limit. Our Max is 20
    '''
#Accumulate and Takewhile
from itertools import accumulate, takewhile

numbers = list(accumulate(range(8))) #Creating list numbers

numbers = list(takewhile(lambda x: x <= 10, numbers)) #This will print numbers less than 10 from the list...

print(numbers)

   ##Output: [0, 1, 3, 6, 10, 15, 21, 28]
'''Notice, how the output looks...it adds the previous to the next and finds the sum, again it has generated a list 
of 8 elements just as we have specified in the range(8).
'''


