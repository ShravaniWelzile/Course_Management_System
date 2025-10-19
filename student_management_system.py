# DATABASES
student_db = {
    101: {'name': 'vaibhav patil', 'course': 'data science', 'total_fees': 40000, 'paid_fees': 30000, 'remaining_fees': 10000}
}
course_fees = {'data science': 40000, 'web development': 30000, 'aws': 15000, 'C++': 25000, 'Java Development': 20000}
users = {'Admin': 'admin123', 'Vaibhav Patil': 'vaibhav123', 'Shravani Welzile': 'shravani123'}

# USER LOGIN
while True:
    print("\nWELCOME TO Shravani's Academy\n")
    username = input("UserName: ")
    password = input("Password: ")
    if username in users and password == users[username]:
        print("Login Successful!")
        break
    else:
        print("Invalid Credentials. Try Again.\n")

print("Shravani's Academy".center(150, '-'))

# MAIN MENU
while True:
    print('''
    ******** HOME ********
    1. Add Student Data
    2. Display Student Data
    3. Update Student Data
    4. Delete Student Data
    5. Filter Student Data
    6. Admin Login  
    7. LogOut                                                                 
    ''')

    try:
        ch = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # 1️⃣ Add Student
    if ch == 1:
        name = input("Name: ")
        courses = list(course_fees.keys())

        print("<= Available Courses => ".center(50))
        for i, course in enumerate(courses, start=1):
            print(f"{i}. {course}")

        try:
            cnum = int(input("Select your Course: "))
            course = courses[cnum - 1]
        except (ValueError, IndexError):
            print("Invalid course selection.")
            continue

        fees = course_fees[course]
        print(f"Fees for {course} is ₹{fees}")

        try:
            dis = float(input("Enter Discount Percentage: "))
        except ValueError:
            print("Invalid discount value.")
            continue

        tfees = fees - fees * dis / 100
        print(f"Fees after {dis}% discount: ₹{tfees}")

        try:
            pfees = float(input("Enter Fees to be paid now: "))
        except ValueError:
            print("Invalid amount.")
            continue

        if pfees > tfees:
            print(f"❌ Amount exceeds total course fees (₹{tfees}). Please pay up to ₹{tfees}.")
            continue

        rfees = tfees - pfees
        reg = max(student_db.keys()) + 1
        student_db[reg] = {'name': name, 'course': course, 'total_fees': tfees, 'paid_fees': pfees, 'remaining_fees': rfees}

        print(f"✅ Data added successfully for {name}!")

    # 2️⃣ Display Student Data
    elif ch == 2:
        print("-" * 135)
        print(f"|{'Reg No':^10}|{'Student Name':^25}|{'Course Name':^25}|{'Total Fees':^15}|{'Paid Fees':^15}|{'Remaining':^15}|")
        print("-" * 135)
        for reg, data in student_db.items():
            print(f"|{reg:^10}|{data['name']:^25}|{data['course']:^25}|{data['total_fees']:^15}|{data['paid_fees']:^15}|{data['remaining_fees']:^15}|")
        print("-" * 135)

    # 3️⃣ Update Student Data
    elif ch == 3:
        try:
            reg = int(input("Enter registration number: "))
        except ValueError:
            print("Invalid registration number.")
            continue

        if reg not in student_db:
            print("Registration number not found.")
            continue

        print('''
        1. Update Name
        2. Update Fees
        3. Change Course
        ''')
        try:
            opt = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input.")
            continue

        if opt == 1:
            uname = input("Enter new name: ")
            student_db[reg]['name'] = uname
            print("✅ Name updated successfully!")

        elif opt == 2:
            print(f"Course: {student_db[reg]['course']}")
            print(f"Total Fees: ₹{student_db[reg]['total_fees']}")
            print(f"Paid Fees: ₹{student_db[reg]['paid_fees']}")
            print(f"Remaining Fees: ₹{student_db[reg]['remaining_fees']}")

            try:
                fees = float(input("Enter additional payment: "))
            except ValueError:
                print("Invalid amount.")
                continue

            if fees <= 0:
                print("❌ Payment must be positive.")
            elif fees > student_db[reg]['remaining_fees']:
                print("❌ Payment exceeds remaining fees.")
            else:
                student_db[reg]['paid_fees'] += fees
                student_db[reg]['remaining_fees'] -= fees
                print("✅ Payment recorded.")
                if student_db[reg]['remaining_fees'] == 0:
                    print("🎉 All fees paid! Thank you!")

        elif opt == 3:
            print(f"Current Course: {student_db[reg]['course']}")
            print("Available Courses:")
            for i, course in enumerate(course_fees.keys(), start=1):
                print(f"{i}. {course}")
            try:
                ch = int(input("Select new course: "))
                new_course = list(course_fees.keys())[ch - 1]
            except (ValueError, IndexError):
                print("Invalid course.")
                continue

            current_pfees = student_db[reg]['paid_fees']
            new_tfees = course_fees[new_course]
            print(f"New Course: {new_course} (₹{new_tfees})")

            if current_pfees >= new_tfees:
                refund = current_pfees - new_tfees
                student_db[reg].update({'course': new_course, 'total_fees': new_tfees, 'paid_fees': new_tfees, 'remaining_fees': 0})
                print(f"✅ Course changed! Refund due: ₹{refund}")
            else:
                rfees = new_tfees - current_pfees
                student_db[reg].update({'course': new_course, 'total_fees': new_tfees, 'remaining_fees': rfees})
                print(f"✅ Course changed! Remaining Fees: ₹{rfees}")
        else:
            print("Invalid option.")

    # 4️⃣ Delete Student
    elif ch == 4:
        try:
            reg = int(input("Enter registration number: "))
        except ValueError:
            print("Invalid number.")
            continue

        if reg in student_db:
            name = student_db[reg]['name']
            del student_db[reg]
            print(f"✅ {name}'s data deleted successfully.")
        else:
            print("Registration number not found.")

    # 5️⃣ Filter Students
    elif ch == 5:
        print('''
        1. By Course
        2. By Pending Fees
        ''')
        try:
            opt = int(input("Filter by: "))
        except ValueError:
            print("Invalid input.")
            continue

        print("-" * 135)
        print(f"|{'Reg No':^10}|{'Student Name':^25}|{'Course Name':^25}|{'Total Fees':^15}|{'Paid Fees':^15}|{'Remaining':^15}|")
        print("-" * 135)

        if opt == 1:
            course_name = input("Enter course name: ")
            for reg, data in student_db.items():
                if data['course'] == course_name:
                    print(f"|{reg:^10}|{data['name']:^25}|{data['course']:^25}|{data['total_fees']:^15}|{data['paid_fees']:^15}|{data['remaining_fees']:^15}|")
        elif opt == 2:
            for reg, data in student_db.items():
                if data['remaining_fees'] > 0:
                    print(f"|{reg:^10}|{data['name']:^25}|{data['course']:^25}|{data['total_fees']:^15}|{data['paid_fees']:^15}|{data['remaining_fees']:^15}|")
        else:
            print("Invalid filter option.")
        print("-" * 135)

    # 6️⃣ Admin Panel
    elif ch == 6:
        password = input("Enter Admin Password: ")
        if password != users['Admin']:
            print("❌ Invalid Admin Password.")
            continue

        print("✅ Admin Login Successful!")
        while True:
            print('''
            ==== ADMIN PANEL ====
            1. Manage Courses
            2. Manage Fees
            3. Manage Users
            4. Back to Main Menu
            ''')
            try:
                adch = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input.")
                continue

            if adch == 1:
                # Manage Courses
                while True:
                    print("\nCourse Management".center(50, '-'))
                    for i, (c, f) in enumerate(course_fees.items(), start=1):
                        print(f"{i}. {c}: ₹{f}")
                    print("1. Add Course | 2. Delete Course | 3. Back")
                    try:
                        subch = int(input("Enter option: "))
                    except ValueError:
                        continue
                    if subch == 1:
                        cname = input("Enter new course name: ")
                        if cname in course_fees:
                            print("Course already exists.")
                        else:
                            try:
                                fee = float(input("Enter course fee: "))
                                course_fees[cname] = fee
                                print(f"✅ Added {cname} (₹{fee})")
                            except ValueError:
                                print("Invalid fee amount.")
                    elif subch == 2:
                        cname = input("Enter course name to delete: ")
                        if cname in course_fees:
                            del course_fees[cname]
                            print(f"✅ Deleted {cname}")
                        else:
                            print("Course not found.")
                    elif subch == 3:
                        break

            elif adch == 2:
                # Manage Fees
                print("\nManage Fees".center(50, '-'))
                for i, (c, f) in enumerate(course_fees.items(), start=1):
                    print(f"{i}. {c}: ₹{f}")
                try:
                    cnum = int(input("Select course to update: "))
                    cname = list(course_fees.keys())[cnum - 1]
                    new_fee = float(input(f"Enter new fee for {cname}: "))
                    course_fees[cname] = new_fee
                    print(f"✅ Fee updated for {cname} (₹{new_fee})")
                except (ValueError, IndexError):
                    print("Invalid input.")

            elif adch == 3:
                # Manage Users
                while True:
                    print("\nUser Management".center(50, '-'))
                    print("1. Add User | 2. Delete User | 3. View Users | 4. Back")
                    try:
                        uch = int(input("Enter your choice: "))
                    except ValueError:
                        continue
                    if uch == 1:
                        uname = input("Enter new username: ")
                        if uname in users:
                            print("User already exists.")
                        else:
                            upass = input("Enter password: ")
                            users[uname] = upass
                            print(f"✅ User '{uname}' added.")
                    elif uch == 2:
                        uname = input("Enter username to delete: ")
                        if uname in users and uname != 'Admin':
                            del users[uname]
                            print(f"✅ User '{uname}' deleted.")
                        else:
                            print("Cannot delete Admin or non-existing user.")
                    elif uch == 3:
                        print("\nCurrent Users:")
                        for u in users.keys():
                            print("-", u)
                    elif uch == 4:
                        break

            elif adch==4:
                #back to main menu
                break
    # 7️⃣ Logout
    elif ch == 7:
        print("Logging Out... Thank You!")
        break

    else:
        print("Invalid Choice.")
