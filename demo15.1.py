#Creating Dictionary Functions
'''
In this demo, we'll get to know how to check if a particular value is present in a dictionary, how to get a particular
value from a dictionary using the get() function and lastly, what to do if the key is not there in the dictionary.

Dictionary format: Key1: Value1, Key2: Value2....
'''

numbers = {
    1: "One",
    2: "Two",
    3: "Three"
}
#print(1 in numbers) #This will check if 1 is present in dict. numbers
print(numbers.get(8, "The Key is not found")) #This will print the value assigned to 1.
'''The String, "The Key is not found" will display coz we want to get a key not defined in our dictionary and so, we 
define the string to be displayed depending on the preferences.
'''
