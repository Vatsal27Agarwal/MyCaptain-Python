#MyCaptain
#School Administration project


import csv

#Function to add info in the csv file
def add_into_csv(info_list):
    with open('student_info.csv','a',newline='') as file:     #append mode starts writing from end of existing content
        w=csv.writer(file)

        if file.tell()==0:                                    #adding header of info just 1 time at the beginning
            w.writerow(['Name','Admission no','class','dob'])  

        w.writerow(info_list)

#Function to take info from user, convert into a list and send the info into csv file using previous function
def takes_info():
    while True:
        info=input('enter info in following format(name admission_no class dob): ')
        info_list=info.split(' ')                           #list of info made

        print('info entered is- \nName: {} \nAdmission no: {} \nClass: {} \ndob:{}'   
              .format(info_list[0],info_list[1],info_list[2],info_list[3]))       

        ch=input('Is the info correct[y/n]: ')              #double check for human error from user side
        if ch=='y':
            add_into_csv(info_list)                         #info added
            print('info added')
            break
        else:
            continue                                        #goes back to start of loop and takes info again


print('This is a School administration program')
takes_info()
ch=input('More students left?[y/n]: ')                       #asks if user wanna end the program 
if ch=='y':
    takes_info()
