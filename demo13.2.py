#Finally block in exception handling
try:
    a = 20
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("There is a divide")
finally:
    print("This will execute no matter what!!")

    '''In the finally block, we write the code that will execute no matter whether the code will run or not, it will
    still execute and it's the last block of exception handling.
    In this case, if we run the code, we'll have two outputs;
            1. There is a divide.
            2. This will execute no matter what!!.
    '''