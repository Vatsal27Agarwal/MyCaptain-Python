#python code for loops

#input according to the values given in the project
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

a=len(list1)
b=len(list2)

#output from list1
print('output1')
for i in range(a):
    if list1[i]>0:
        print (list1[i])
    else:
        continue

#output from list2
print('\noutput2')
i=0
list3=[]
while i<b:
    if list2[i]>0:
        list3.append(list2[i])
    i=i+1
print(list3)
