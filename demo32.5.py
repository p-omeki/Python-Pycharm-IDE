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
