#Exception handling in Python
'''
Exception prevent one from executing a code further after the error has occured in  his/her code.
So, in this demo, I'll show you how to bypass the error and execute code that follow after the exception occurs.
'''
try: #We run the code that we think we'll give an exception error in this try block
    a = 20
    b = 0
    print(a/b)  #This will give a divide by zero error
except ZeroDivisionError:  #Confirms there is a divide by zero error in the code and continues with the execution of l11
    print("There is a divide by zero error in the code")
    '''Probably wondering what might happen if there would be no ZeroDivisionError?
    The code in the try block will be executed and line 11(l11) would not be executed. 
    We now have a brief understanding of exception, let's tall about finally block in demo13.2
    '''
