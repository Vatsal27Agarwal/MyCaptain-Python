#Assignments by Gowtham Bhaiya

#My Assignment - 1.1
'''
1. try out logical operators

2. try out comparison operators
'''


#1
a=10
b=5
c=1

#three logical operators are there: (and,or,not)

#and operator: both conditions need to be true
if a%2==0 and c//2==0:
    print('and operator working')

#or operator: any one condition need to be true
if b%2==0 or c//2==0:
    print('or operator working')

#not operator: condition need to be false 
if not(b%2==0):
    print('not operator working')


#2
a=10
b=5
c=1
d=-10
e=5

#six comparison operators: (>,<,==,!=,>=,<=)

#> : greater than operator
if a>b:
    print('greater than operator working')

#< : less than operator
if d<0:
    print('less than operator working')

#== : equal operator
if b==e:
    print('equal operator working')

#!= : not equal operator
if a!=e:
    print('not equal operator working')

#>= : greater than equal to operator
if b>=e and c>=d:
    print('greater than equal to operator working')

#<= : less than equal to operator
if e<=b and d<=a:
    print('less than equal to operator working')











