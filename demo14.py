#File handling in Python
'''
File handling deals with the writing and reading of files one is using in his code or the databases.
In this part, we'll create a .txt file which we'll write, "w" and read, "r" to it.
We've created a demo14.txt.py file...
'''
file = open("demo14.txt.py", "w")
'''On the above line of code, we've initialized the file to be opened using the function open() which we have 
passed parameters inside. The first parameters we have is the file name that we need to pass the file name we'll access
and the second parameter is the mode we want to use to access the file, either write or read mode.
'''
# This will write on the file

file.close() #Always close your file to avoid errors when running your file