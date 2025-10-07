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

        print("<= Available Courses => ".center(50))

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
        #update
        cont=True
        while cont:
            reg=int(input("Enter registraion number: "))
            if reg in student_db:
                cont=False

        
        print('''
            1.Name
            2.Fees
            3.Change Course   
                ''')
        ch=int(input("Enter your choice: "))
        if ch==1:
            #name
            uname=input('Name: ')
            #var[key]=uvalue
            student_db[reg]['name']=uname
            print(" Name Updated Successfully !")

        elif ch==2:
            #Fees
            print(f'Course Name:{student_db[reg]['course']}\nTotal Fees:{student_db[reg]['total_fees']}\nPaid fees:{student_db[reg]['paid_fees']}\nRemaining Fees:{student_db[reg]['remaining_fees']}\n ')
            fees=eval(input("Enter Amount: "))
             #var[key]=uvalue
            
            student_db[reg]['paid_fees']+=fees
            student_db[reg]['remaining_fees']-=fees
            print("Thank You ! ")


        elif ch==3:
            #course updation 
            '''display
            '''
            print("============ Current Course Details ============ ")
            print(f'Course Name:{student_db[reg]['course']}\nTotal Fees:{student_db[reg]['total_fees']}\nPaid fees:{student_db[reg]['paid_fees']}\nRemaining Fees:{student_db[reg]['remaining_fees']}\n ')
            
         
            courses=list(course_fees.keys())
            print("================================================")
            print("<= Available Courses => ".center(50))
            sr=1
            for course in courses:
                print(f'{sr}.{course}')
                sr=sr+1

            print("============================")

            while True:
                ch_course_select=int(input("Select new course: "))
                if 1<= ch_course_select <=len(courses):
                    index=ch_course_select-1
                    new_course=courses[index]
                    break
                else:
                    print("Invalid Course number, Please Select Valid Number ")
        
            print(f'New Course Selected : {new_course}')

    
            #Fees Calculation for new course
            current_pfees=student_db[reg]['paid_fees']
            new_tfees=course_fees[new_course]   #without discount

            print(f'Total Fees for New Course {new_course} (*without discount*) is {new_tfees}')

            fees_diff=current_pfees-new_tfees

            if fees_diff>=0:
                refund=fees_diff
                new_pfees=new_tfees
                new_rfees=0
                print(f"\n Your already paid fees {current_pfees} covers new course {new_course}'s fees {new_tfees}")
                if refund>0:
                    print(f"***Refund Amount : {refund} ***")

            else:
                new_pfees=current_pfees
                new_rfees=abs(fees_diff)
                print(f"\n Your already paid fees {current_pfees} is less than new course {new_course}'s fees({new_tfees})")
                print(f"Remaining amount to be paid : {new_rfees}")

            
        else:
            print("Invalid input !!!")



    elif ch==4:
        #delete
        while True:
            reg=int(input("Enter Registration Number: "))
            if reg in student_db:
                break

        n=student_db[reg]['name']
        student_db.pop(reg)
        print(f"{n}'s data is deleted Successfully !")



    elif ch==5:
        #filter
        print('''
            1.Course
            2.Remaining Fees
            ''')
        ch=int(input("Filter By:"))
        if ch==1:
            #tables logic
            print("-"*135)
            print(f'|{'Reg No':^20} | {'Student Name':^20}| {'Course Name':^20} | {'Total Fees':^20}| {'Paid Fees':^20}| {'Remaining Fees':^20}|')
            print("-"*135)    

            for reg in student_db:
                print(f'|{reg:^20} | {student_db[reg]['name']:^20}| {student_db[reg]['course']:^20} | {student_db[reg]['total_fees']:^20}| {student_db[reg]['paid_fees']:^20}| {student_db[reg]['remaining_fees']:^20}|')
                print("-"*135)

        elif ch==2:
            pass
        else:
            print("Invalid input...")


    elif ch==6:
        print("Thank You ! ")
        break
    else:
        print("Invalid Choice")
