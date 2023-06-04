#Regular Expression in Python
'''
Regular expression is a module that allows us to modify strings in python. Regular expression is used perform to major
tasks in python, this includes;
 1. Checking if a string matches a particular pattern.
 2. Perform substitution in strings.
'''
# Match function in Regular Expression
import re
Rpattern = r"mail"  #The 'r' prefix is used to create raw strings for our pattern, in this case, 'mail'
if re.match(Rpattern, "mailpartymeki@gmail.commailpatohmail"):
   print("Match Found")
else:
   print("No Match Found")
'''Notice, that if we put any name first aprt from mail, we find a "No match found", that's what the match function 
actually does, and so, that's an disadvantage, so how do we fix this?. We're going to use the search function, this will
look for the mail pattern anywhere around your string.Lastly, we have the findall function that checks the number of 
times the 'mail' is present in the the string.
Check the example below...
'''
#We using the same import re and Rpattern, so we'll continue from if...
if re.search(Rpattern, "mekimailpartymeki@gmail.commailpatohmail"):
   print("Match Found")
else:                         #This will print a Match Found coz the 'mail', is not necessarily at the start but somewhere in the string.
   print("No Match Found")
#Findall function now,
'''
if re.findall(Rpattern, "mekimailpartymeki@gmail.commailpatohmail"):
   print("Match Found")
else:
   print("No Match Found")
   '''
print(re.findall(Rpattern, "mekimailpartymeki@gmail.commailpatohmail")) #This will print the exact word, 'mail' 4 times as we've used in our string.


