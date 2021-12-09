#project 1


# part1 - computing area

#imporing maths module to get the value of pi
import math

r=float(input("enter radius: "))
p=math.pi

#calculating area
a=p*r*r

print("The area is: ", a)



#part 2 - printing extension of a file name

fn= input("Enter Filename: ")

#separating the name and the extension
f = fn.split(".")

print ("Extension of the file is : " + f[-1])
