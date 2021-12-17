#Assignments by Gowtham Bhaiya

#My Assignment - 1.2
'''
build a calculator
'''

#Functions available in the calculator(+,-,*,/,//,%,**)

#assigning variable values to the function
a='+'         #addition
s='-'         #subtraction
m='*'         #multiplication
d='/'         #division
fd='//'       #floor division
mod='%'       #modulus
power='**'    #power
e='='         #equal to

#will print the result after every result so that user knows the calcutions the user is doing
while True:
    ch=input('want to use the calculator(y/n): ')     #asking if the user wants to use the calculator
    if ch=='n':
        break                           #turning off the calculator
    
    else:
        num1=float(input('enter number: '))  
        func1=input('enter func: ')  
        num2=float(input('enter number: '))
        
        if func1==p:
            ans=num1+num2
            print(ans)
        elif func1==s:
            ans=num1-num2
            print(ans)
        elif func1==m:
            ans=num1*num2
            print(ans)
        elif func1==d:
            ans=num1/num2
            print(ans)
        elif func1==fd:
            ans=num1//num2
            print(ans)
        elif func1==mod:
            ans=num1%num2
            print(ans)
        elif func1==power:
            ans=num1**num2
            print(ans)
        else :
            print('function not available')
            continue                                #will again ask for 2 numbers and a function

        #adding all if...elif situations again in case the user wants to use calculator on the same result
        
        func='+'                                    #assigning some value to variable 'func' to run the while loop
        while func != '=':
            func=input('enter func (enter = for final result): ')   #considering '='(for result) as a function too
            if func!='=':
                num=float(input('enter number: '))  #will just print out result if '=' is inputted
                
            if func==p:
                ans=ans+num
                print(ans)
            elif func==s:
                ans=ans-num
                print(ans)
            elif func==m:
                ans=ans*num
                print(ans)
            elif func==d:
                ans=ans/num
                print(ans)
            elif func==fd:
                ans=ans//num
                print(ans)
            elif func==mod:
                ans=ans%num
                print(ans)
            elif func==power:
                ans=ans**num
                print(ans)
            elif func==e:
                print('the final result calculated is: ',ans)    #after printing final result will go back to start of loop
            
        
            
