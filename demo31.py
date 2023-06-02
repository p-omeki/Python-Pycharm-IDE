#Data hiding or encapsulation in Python
'''
Encapsulation in python in layman's language is simply hiding a part of your code from being visible to other users.
In more simple terms, it's referred to us data hiding. In python, to encapsulate a aprt of your code we use '__' or
dandass or double underscores before the code we want to encapsulate...
Check the code below...
'''
class EnCap:
    __hideVariable = 0

    def __add__(self, increament):
        self.__hideVariable += increament
        print(self.__hideVariable)

ObjeEncap = EnCap()
ObjeEncap.__add__(5)