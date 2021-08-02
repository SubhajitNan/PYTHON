#A Python program which accepts the radius of a circle from the user and computes area.

from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

Sample Output:-

Input the radius of the circle : 1.1                                                                          
The area of the circle with radius 1.1 is: 3.8013271108436504 

**********************************************************************************************************

#A Python program which accepts the filename from the user and print the extension for that.

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))

Sample Output:-

Input the Filename: abc.python
The extension of the file is : 'python'

**********************************************************************************************************
