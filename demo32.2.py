#The Dot Metacharacter
'''
The Dot Metacharacter simply allows us to perform powerful regular expression. We use the '.' just like the name
suggests. There are two more significant metacharacter in Python that we use, this includes: caret(^) and dollar(&).
In the example below, we'll discuss the dot.
'''
#The Dot (.)
import re
Rpattern = r"Gr.y" #What the '.' will do, it will allow any character to be put in the '.' position
if (re.match(Rpattern, "Grxy")): #Any letter we put in between Gr and y is acceptable, i.e a,e,x,b,z,k,d,p,t,b, anything.
    print("Match Found")
else:
    print("No Match Found")