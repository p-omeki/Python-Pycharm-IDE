#List slicing in Python
'''
List slicing comes from lists in python, and it basically means, cutting down our list data, and so we do not have a
full list when we print it out.
Further explanation on the example below...
'''
numbers = [0, 10, 20, 30, 40, 50, 60, 70, 80] #We declare our list

print(numbers) #This will print our full list. And what if we don't want the full list? This is where the list slicing comes in.

print(numbers[1:5]) #This will slice our list and start printing from index 2 to 5.

'''We can also specify the interval we want the list to be sliced. The interval will depend on the size of your list and 
in our case we going to use interval 2.
Check the print below...
'''
print(numbers[1:8:2]) #2 is the interval and we'll be skipping one index to the next in the printout.