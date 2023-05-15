#We will do our first coding challenge in Pycharm, and we'll find the Simple Interest.
p = input ("Enter value for P: ")
n = input ("Enter value for N: ")
r = input ("Enter value for R: ")

p = int(p)
n = int(n)     #This will convert the values inserted as strings above to integers.
r = int(r)

#We'll specify Simple Interest as 'si()'

si = (p*n*r)//100   #The double forward slash removes the floating point value in our final ans.

print (si)

   # p stands for principle
   # n stands for number of users
   # r stands for rate of interest
'''
Now, the above values are in the form of strings. And we want them to be in integer form, so, how are we 
going to do it. We will declare an int() and pass the arguments p, n, and r respectively.
'''
