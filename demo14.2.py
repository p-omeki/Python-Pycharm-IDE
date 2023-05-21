#Writing file in Python
file = open("demo14.txt", "w")
file.write("This is the first line we've written")
file.close()
"""The first block above, in line 1 we've opened our file and passed mode write, "w" which will write our text to the 
.txt file from python file direct.
"""

file = open("demo14.txt", "r")
content = file.read()
print(content)
file.close()
"""The second block above, notice the difference between write and read. 3 & 4 lines of code respectively. In this block,
we declare the variable content which we use to store the .txt file and print it out.
"""

file = open("demo14.txt", "a")
file.write("\n This is the second line we've written")
file.close()
"""In this block above, the "w" mode will override the 1st "write" in the first block and so, how do we solve this?
We'll use the append(), "a" to enable prevent it from overriding the first write line.
In place of "w" replace it with "a".
"""