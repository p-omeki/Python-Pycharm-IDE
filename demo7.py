#Boolean logic in Python
'''
Boolean are used whenever u need to check multiple condition to execute a code.
The main boolean operators we use in Python is the logical and & logical or. For logical AND, all the conditions must
be TRUE for the line of code to be executed while logical OR, only one of the statement needs to be TRUE for the
code to execute.
Below, we're going to create a simple login system that we'll use boolean logic to verify the conditions.
'''

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "admin2023":
    print("Valid User")
else:
    print("Invalid User")