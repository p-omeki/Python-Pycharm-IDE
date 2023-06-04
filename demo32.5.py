#Meta (*) character
'''
This metacharacter matches zero or more than one occurrence of the preceding character or group.
The group is denoted by ().
Check the example below...
'''
import re

Rpattern = r"mail(mine)*"
if re.match(Rpattern, "mail(mine)partymeki@gmail.commailmine"):
    print("Match Found")
else:
    print("Not Found")
'''In line 10 of our code, if we remove the 'mail' we'll have a -ve response coz we would have removed the initialized 
string 'mail' which is the main string. The string enclosed with bracket/ also a (group), '(mine)' now is the primary
string and we will get a +ve response if we run or not run the string without it...
In summary, the group indicates that we can have the string, zero, once or more than one number of times when we run 
our String.
'''
