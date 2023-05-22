#Tuples in Python
'''
Tuples as similar to list with some sligh differences. So, what are tuples? Tuples are immutable data structures
which u can't change the value after storage. In lists, u can change the value after storage and this the main
difference.
Also, list items are enclosed inside a square [] bracket while in tuples, we use parenthesis, () .
In tuples also, u can run it without the () and still found no errors.
'''

#fruits = ("Apples", "Mango", "Banana", "Peach")
fruits = "Apples", "Mango", "Banana", "Peach" #This will assign values to the tuples
'''How do we show that tuples are immutable and what's immutable? Tuples being immutable means that u cannot change 
the values in the tuples once assigned. 
Check the code line before where we'll try changing the tuple referenced by index[0]....
'''
#fruits[0] = "Avocado" #This will generate an immutable error since we trying to change the value of index[0].

print(fruits[0])