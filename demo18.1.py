#String functions in python
'''
String functions are mostly used in web development and one ca use them based on the need at hand.
In this demo however, we're going to discuss a few of the functions. That is, .join, .replace, .startswith, .endswith
.upper and lastly .lower.
I'll give a brief info about the function in their respective lines...
'''
#Join function ~ Basically joins a string with arguments passed under the join function.
newstring = ":" #This will join our list with a : when we run the printout
print(newstring.join(["Apple", "Mango", "Banana"]))

#Replace function
newstring = "Hello there" #We first define our string...
print(newstring.replace("there", "World")) #Here, we first define the string we want to replace,"there" followed by the
                                            # second string, "World" to take position.
#Startswith function ~ Checks if our string starts with a particular word. In our case, "This".
newstring = "This is a new string we've created"
print(newstring.startswith("This")) #This will print either True or False depending on what we've specified.

#Endswith function ~ Checks is our string ends with a particular word. in our case, "created"
newstring = "This is a new string we've created"
print(newstring.endswith("created"))

#Upper function ~ Prints our string to capital letters
newstring = "This is a new string we've created"
print(newstring.upper())

#Lower function ~ Prints our string to small letters
newstring = "This is a new string we've created"
print(newstring.lower())
