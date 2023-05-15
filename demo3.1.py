#List operations in Python

numbers = [1,1,1,1,1]
#numbers[2] = 5 #Here, we're specifying index 2 value and re-assigning it value 5 and this will change the output.

print(numbers)
print(numbers*3) #Here, this will print our list 3 times and we'll have 15 "1's"

'''
Have u asked yourself how you would check if a particular item is present in the list or not? Well, the below
code about fruit I'll you just how you can do it using the "in" function. 
Check the code below...
'''
fruits = ["Apple", "Orange", "Mango", "Banana"] #We've declared a new list called fruits.

print("Apple" in fruits)
'''The above code will print TRUE since Apple is in fruit list. If we put a fruit name not present in our fruit list,
it will printout a FALSE output since the item is not in the fruits list.
In summary, the keyword here is "in" function which we use to check if a particular item is present in a list or not.
'''

