#Code Re-use and Functions in Python
'''
What's code re-us?. I would define it as a capability that allows us to use a code a number of times in our projects
and how does it relate with functions?.
What is function? Functions I would term is as defined lines of code waiting to be called for execution.
So, the relation between code re-use and function is that, function allows code to be defined within it and called for
execution in different places in our code without having to write the code again, this act of calling a function's lines
of code using it in different places in out code is now code re-use and that's there relation.
'''

#I'll create a random code to show what have just explained above...

print("Patrick")
print("Kabarak University")
print("Nakuru County")


print("Patrick")                   #Now, what I have done here is that I have reused the code above.
print("Kabarak University")     #And probably, u may ask yourself what will happen if we need to use the code multiple times?
print("Nakuru County")        #That's where we introduce funtion and define this code inside the function.

#Defining a function for the code above

def function1():
    print("Patrick")
    print("Kabarak University")
    print("Nakuru County")

function1()   #This will call the function1 for execution.

'''In summary, the function1 defined will help us to avoid having to write the code over and over again and also ease 
the editing of the code and we'll simply just edit the function1 alone and save ourselves the need to edit each line of
code.
'''

