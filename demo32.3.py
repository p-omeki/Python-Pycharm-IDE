#Caret and Dollar Metacharacter
'''
The metacharacters are used to specify the starting point and ending point of a string respectively. That is, ^ & $.
They're majorly used in web frameworks such as Django to specify the URl pattern of a website one is creating.
'''
import  re
Rpattern = r"^Gr.y$" #We've specified our string to start with G and end with y, so any change we'll result to negative response.
if (re.match(Rpattern, "Jray")): #If we try to change the starting point G or Y we get -ve feed, in our case replace G with J
    print("Match Found")
else:
    print("No Match")

    #Check Demo32.2 for more info...
