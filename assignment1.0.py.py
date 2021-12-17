#Assignments by Gowtham Bhaiya

#My Assignment - 1.0
'''
1. 10, 1, 8, 3, 6, 5, 4, 7, x, y
   Find the general solutions of x and y.
   write an algorithm for the same.

2. Check out floor division with 3 different values.
'''

#1
list1= [10,1,8,3,6,5,4,7]
'''by observation every odd placed number is decreasing by 2
and every even placed number is increasing by 2'''

#general solution by basic deduction for x,y are:
x=2
y=9

list1.append(x)
list1.append(y)
print(list1)

#algorithm
list2= [10,1,8,3,6,5,4,7]
ch='y'
while ch=='y':
    l=len(list2)
    if l%2==1:
       a= list2[l-2] + 2
       list2.append(a)
    else:
       a= list2[l-2] - 2
       list2.append(a)
    print(list2)
    ch=input('wanna continue(y/n): ')

#2

#checking i1//12 with 3 diff values
for i in range(3):
    i1=int(input('enter 1st number: '))
    i2=int(input('enter 2st number: '))
    ans=i1//i2
    print(ans)



















    
