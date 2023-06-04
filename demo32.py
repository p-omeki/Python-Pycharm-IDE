#Regular Expression in Python
'''
Regular expression is a module that allows us to modify strings in python. Regular expression is used perform to major
tasks in python, this includes;
 1. Checking if a string matches a particular pattern.
 2. Perform substitution in strings.
'''
import re
Rpattern = r"mail"  #The 'r' stands for raw and it initialize the string we want to check the pattern for, in this case, 'mail'
if re.match(Rpattern, "partymeki@gmail.com"):
   print("Match Found")
else:
   print("No match found")