import sqlite3

db_file = sqlite3.connect("student.db")
cur = db_file.cursor()

print("+++++++++++++++Welcome To our Student Database++++++++++++++++")
print("")
user_input = input("What do you want to do ? [add/Find] students: ").lower()
if (user_input == 'add'):
    std_number = int(input("How many do you want to add? "))
    i = 1
    while (i <= std_number):
        print("=================Student{} Personal Info=====================".format(i))
        print("")
        fname = input("Please insert student firstName: ")
        lname = input("Please insert student LastName: ")
        email = input("Please insert student email address: ")
        phone = input("Please insert the student phone number: ")
        std_tuple = tuple([fname, lname, email, phone])
        cur.execute("INSERT INTO student_info(fname, lname, email, phone) values(?,?,?,?)", std_tuple)
       
            
        print("==================Student {} Emergency Contact=========================".format(i))
        print("")
        eName = input("In case of Emergency who should we contact[insert the name]?:  ")
        eEmail = input("Please insert the person email address: ")
        ePhone = input("Please insert hus phone number: ")
        emergency_contact = tuple([eName, eEmail, ePhone])
        cur.execute("INSERT INTO emergency_contact(parents_tutor_name , eEmail, ePhone) VALUES(?, ?, ?)", emergency_contact)
        
            
        print("====================Student {} GPA===============================".format(i))
        print("")
        gpa_input = float(input("Please insert the student GPA: "))
        cur.execute("SELECT * FROM student_info")
        last_id = cur.fetchall()[-1]
        next_id= last_id[0]+1
        gpa_tuple = tuple([next_id, next_id, gpa_input])
        cur.execute("INSERT INTO student_gpa(id , emergency_id, gpa) VALUES(?,?,?)", gpa_tuple)
        db_file.commit()
        i +=1

elif(user_input == 'find' ):
    a = input("Choose between [single/all] student: ").lower()
    if (a == 'single'):
        p_input = input("Enter student phone number: ")
        phone = tuple([p_input])
        print(phone)
        cur.execute("""SELECT std.id, std.fname, std.lname, std.email, std.phone,
                    emc.parents_tutor_name as Emergency, emc.eEmail, emc.ePhone,
                    gpa.gpa
                    FROM student_info as std 
                    INNER JOIN emergency_contact as emc 
                    ON std.id = emc.id 
                    INNER JOIN student_gpa as gpa 
                    ON emc.id = gpa.id 
                    WHERE std.phone = ? """, phone)
        output = cur.fetchall()
        for i in output:
            print (i)
        db_file.commit()
    elif (a == 'all'):
        cur.execute("""SELECT std.id, std.fname, std.lname, std.email, std.phone,
                    emc.parents_tutor_name, 
                    emc.eEmail as parent_email,
                    emc.ePhone as parent_contact,
                    gpa.GPA as GPA
                    FROM student_info std
                    INNER JOIN emergency_contact emc
                    ON std.id = emc.id
                    INNER JOIN student_gpa as gpa
                    ON emc.id = gpa.id
                """)
        output = cur.fetchall()
        for item in output:
            print (item)
        db_file.commit()
       
            
    else:
        print("wrong Input")
else:
    print("wrong input")


