#Creating a Grading System using elif Statement
'''
Now, the major difference between if statement and elif statement is that in elif statement, we can execute multiple conditions while
in if statement, we can only execute one condition.
'''

marks = int(input("Enter your marks: ")) #This will print the string value direct to integer.
if marks > 70:
    print("First class honours")
elif marks > 60:
    print ("Second class honours")
elif marks > 50:
    print ("Pass")
elif marks > 40:
    print ("Fail")
else:
    print ("Get a life Bro!\n It's over.")