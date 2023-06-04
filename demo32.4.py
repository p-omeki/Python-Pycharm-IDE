#Character Class in Regular Expression
'''
The character class is used to match one of a specific class set to a particular character. In our case, we're going to
to check a character class for car plates in kenya, new place #KDA 001
'''
import re
Rpattern = r"[A-Z][A-Z][A-Z] [0-9][0-9][0-9][A-Z]"
EnterPlate = input("Enter Plate Number: ")
if re.search(Rpattern, EnterPlate):
    print("Match Found")
else:
    print("No Match Found")