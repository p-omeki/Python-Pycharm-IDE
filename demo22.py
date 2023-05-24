#Maps in python
'''
We use Maps to perform operations on a list. Basically, it main significance in Python is that it's used to manipulate
list values.
You can use functions and lambdas when perfoming an operation in list.
Check the code below...
'''
'''def add(x):  #We define the function add().
    return x+2
    '''
  #Notice, no print in this line...  i.e print(add(4))
newlist = [5, 10, 15, 20, 25, 30] #We define the list we intend to manipulate...in our case "newlist".

##result = list(map(add, newlist))

#What if we use lambda?
result = list(map(lambda x: x+2, newlist)) #Notice, we've removed the function

print(result)  #The integers in our list will act as our "x".
