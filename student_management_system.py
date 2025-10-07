student_db={101:{'name':'vaibhav patil','course':'data science','total_fees':400000,'paid_fees':30000,'remaining_fees':10000}}
course_fees={'data science':40000,'web developement':300000,'aws':15000,'C++':25000,'Java Development':20000}

print("Shravani's Academy".center(100,'-'))

while True:
    print('''
    1.Add Student Data
    2.Diplay Student data
    3.Update Student Data
    4.Delete Student Data
    5.Filter Student Data  
    6.LogOut                                                                 

    ''')

    ch=int(input("Enter your choice: "))
    if ch==1:
        name=input("Name: ")
        courses=list(course_fees.keys())

        print("<= Available Courses => ")

        sr=1
        for course in courses:
            print(f'{sr}.{course}')
            sr=sr+1

        ch=int(input("Select your Course: ")) 
        index=ch-1

        course=courses[index]
        print(course)

        #accessing fees from course name in dict
        fees=course_fees[course]
        print(f"fees for course {course} is {fees}")
        
        #discount
        dis=eval(input("Enter Discount Percetage: "))
        tfees=fees-fees*dis/100
        print(f'fees after {dis}% discount is {tfees}')

        pfees=eval(input("Enter Fees to be paid now: "))
        rfees=tfees-pfees

        print(f" Total Fees(after discount) : {tfees} \n Paid Fees: {pfees} \n Remaining Fees: {rfees}")

        #adding values to db (student_db ) dict
        #var[key]=value

        reg=len(student_db)+101
        student_db[reg]={'name':name,'course':course,'total_fees':tfees,'paid_fees':pfees,'remaining_fees':rfees}
        print("Data Addded to Database Successfully !!!")

        #print(student_db)



        #Add student data
    elif ch==2:
        print("-"*135)
        print(f'|{'Reg No':^20} | {'Student Name':^20}| {'Course Name':^20} | {'Total Fees':^20}| {'Paid Fees':^20}| {'Remaining Fees':^20}|')
        print("-"*135)    

        for reg in student_db:
             print(f'|{reg:^20} | {student_db[reg]['name']:^20}| {student_db[reg]['course']:^20} | {student_db[reg]['total_fees']:^20}| {student_db[reg]['paid_fees']:^20}| {student_db[reg]['remaining_fees']:^20}|')
             print("-"*135)   

        #Display 
    elif ch==3:
        pass
        #update
    elif ch==4:
        pass
        #delete
    elif ch==5:
        pass
        #filter
    elif ch==6:
        print("Thank You ! ")
        break
    else:
        print("Invalid Choice")