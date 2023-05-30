#Sets in python
'''
Sets are similar to lists. The only difference between them is there declaration, {} for sets and [] for list, and also
in sets, the elements declared are uniques, and it allows no duplicate values to be stored whereas in Lists, u can store.

Check the example below...
'''
#Creating a set of 'numbers'
numbers = {1, 2, 3, 4, 5} # ~ Set don't accept duplicate elements, so if we add 2 to the set, it will print a single 2.
#How about we add a number to the set?
numbers.add(6)  #This will add '6' to our set
#How about we remove a number from our set
numbers.remove(4) #This will remove '4' from our set

print(numbers)

#Now, let's find how to find a Set Union, Intersection and Difference.
## Set Union
'''Set Union, what it will do, it will merge set A and set B and notice, both sets have 5 and 6. Since set don't allow 
duplicate elements, it will not repeat 5 and 6 twice, rather print it once.

Set Union is denoted by '|'
'''
setA = {1, 2, 3, 4, 5, 6}
setB = {5, 6, 7, 8, 9, 10}

print( setA | setB)
## Set Intersection
'''The set intersection will check for the most common numbers in between the set and where they meet and print them 
out. in our case it's 5 and 6.

Set intersection is denoted by '&'
'''

setA = {1, 2, 3, 4, 5, 6}
setB = {5, 6, 7, 8, 9, 10}

print(setA & setB)
## Set Difference
'''Set difference will check for number repeating itself in setA and setB, now notice we subtracting setB from setA,
this will check the repeating numbers in setB that also in setA and remove them, in our case, 5 and 6.

Set difference is denoted by '-'
'''
setA = {1, 2, 3, 4, 5, 6}
setB = {5, 6, 7, 8, 9, 10}

print(setA - setB)