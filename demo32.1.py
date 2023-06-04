#Find and Replace in Python
'''
Find and Replace is used in Regular Expression to replace a word in a string and so, we need to find and replace it.
'''
import re
string = "My name is Patrick,\n Hey, I'm Patrick"
Rpattern = r"Patrick" #We find the string Patrick which we'll want to replace.
NewString = re.sub(Rpattern, "Meki", string) #The sub fn replaces the string Patrick with 'Meki' and of course, and
                                             #so we pass string and Rpattern as arguments.                                                 #
print(NewString)