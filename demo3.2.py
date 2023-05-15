#List functions
'''Let's say u you want to add an item to your list. In this case, fruits is our list.
We'll use an "append()" function which allows us to have additional items added to our list.
See example below...
'''
fruits = ["Apple", "Orange", "Mango", "Banana"]
fruits.append("Avocado") #This will add Avocado to our fruits list.

print(fruits)

#How about we calculate the length of our list?

print(len(fruits)) #Notice, we've used len() function shortform of length. This will give the total number of items in our list.

#How about we insert an item to our list?
'''The insert function is similar to append function and there's only one major difference between them is that;
In append(), the item added to the list is positioned at the end of the list items while in insert(), you can
specifically decide which position the item would occupy in the list by first declaring the position you want
the item to be followed by the item name.
Check the example below...
'''
fruits.insert(1, "Avocado") #This will print Avocado to position (index) 1 of the list

print(fruits)

#How about we want to check a particular item position in our list position?

print(fruits.index("Mango")) #This will print out the position of Mango in our list giving out its index.