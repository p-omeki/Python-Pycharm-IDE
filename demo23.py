#Filters in Python
'''
Filters as the name suggest, they're used in conjunction with lambdas to filter out some values from a list.
Check the example below...
'''

newlist = [2, 3, 4, 7, 8, 9, 4, 5, 8, 3, 2, 1, 56, 12, 23, 67, 78, 98, 10, 14, 44] #We first define the list

result = list(filter(lambda x: x % 2 == 0, newlist)) #We've specified the list to be printed to only contain even numbers.

print(result)