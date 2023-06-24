nm = str(input("Enter Your Name :")) #Name
ag = int(input('Enter Your Age  :')) #Age
by = int(2023-ag)#Birth Year

if ag<16:
    print('Sorry,',nm,' You Can''t Continue')
    print('Good Bye,',nm)
    
else:
    print('Let us Continue ...')
    print(nm,' Enter Your ID card Number (Enter Numbers Seperately)')
    if by>2000:  # After 2000
        n1 = int(input('Enter 1st Number : '))
        n2 = int(input('Enter 2nd Number :'))
        n3 = int(input('Enter 3rd Number :'))
        n4 = int(input('Enter 4th Number :'))
        n5 = int(input('Enter 5th Number :'))
        n6 = int(input('Enter 6th Number :'))
        n7 = int(input('Enter 7th Number :'))
        n8 = int(input('Enter 8th Number :'))
        n9 = int(input('Enter 9th Number :'))
        n10 = int(input('Enter 10th Number:'))
        n11 = int(input('Enter 11th Number :'))
        n12 = int(input('Enter 12th Number :'))
        sum = int(n5*100 + n6*10 +n7)
        if sum>=500:
            gender =str("Female")
            sum = sum-500
        else :
            gender = str("Male")

        if sum<=31:
            month = str("January")
            date  =  sum
        elif sum<=60:
            month = str('February')
            date = sum - 31
        elif sum<=91:
            month = str('March')
            date = sum - 60
        elif sum<=121:
            month = str('April')
            date = sum - 91
        elif sum<=152:
            month = str('May')
            date = sum - 121
        elif sum<=182:
            month = str('June')
            date = sum - 152
        elif sum<=213:
            month = str('July')
            date = sum - 182
        elif sum<=244:
            month = str('August')
            date = sum - 213
        elif sum<=274:
            month = str('September')
            date = sum - 244
        elif sum<=305:
            month = str('October')
            date = sum - 31
        elif sum<=335:
            month = str('November')
            date = sum - 305
        else:
            month = str('December')
            date = int(sum - 335)
 #########################################################################################################           
    else:  #Before 2000
        n1 = int(input('Enter 1st Number : '))
        n2 = int(input('Enter 2nd Number :'))
        n3 = int(input('Enter 3rd Number :'))
        n4 = int(input('Enter 4th Number :'))
        n5 = int(input('Enter 5th Number :'))
        n6 = int(input('Enter 6th Number :'))
        n7 = int(input('Enter 7th Number :'))
        n8 = int(input('Enter 8th Number :'))
        n9 = int(input('Enter 9th Number :'))
        sum = int(n3*100 + n4*10 +n5)
        if sum>=500:
            gender =str("Female")
            sum = sum-500
        else :
            gender = str("Male")

        if sum<=31:
            month = str("January")
            date  =  sum
        elif sum<=60:
            month = str('February')
            date = sum - 31
        elif sum<=91:
            month = str('March')
            date = sum - 60
        elif sum<=121:
            month = str('April')
            date = sum - 91
        elif sum<=152:
            month = str('May')
            date = sum - 121
        elif sum<=182:
            month = str('June')
            date = sum - 152
        elif sum<=213:
            month = str('July')
            date = sum - 182
        elif sum<=244:
            month = str('August')
            date = sum - 213
        elif sum<=274:
            month = str('September')
            date = sum - 244
        elif sum<=305:
            month = str('October')
            date = sum - 31
        elif sum<=335:
            month = str('November')
            date = sum - 305
        else:
            month = str('December')
            date = int(sum - 335)

    print('Your Gender = ',gender)
    print('Your Birthday = ',date,'/',month,'/',by)


        
         
        


    
        
    
    





            