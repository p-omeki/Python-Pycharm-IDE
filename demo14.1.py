#Reading file in Python
file = open("demo14.txt", "r") #This will read the file demo14.txt
#content = file.read() #This will read all the lines of code we have in our .txt file
content = file.readline() #Will print ONLY the first line or single line of code
print(content) # This will print out the .txt file
'''In the file.read() function, notice we've spacified also a variable content which we'll use to store the data
that we've read from the .txt.
Also, inside the file.read(), we may pass some parameter to either specify bits of line to be printed out,
e.g file.read(10) will only print out 10 bits of code

N/B: In read file, we update the .txt file manually while in write mode, we'll update it from the code and it updates
automatically to the .txt file.
'''
file.close() #Always close your file to avoid errors during execution