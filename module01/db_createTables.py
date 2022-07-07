import sqlite3

db_file = sqlite3.connect("student.db")
cur = db_file.cursor()

#create a table called student_info 
cur.execute( """
            CREATE TABLE IF NOT EXISTS student_info 
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fname TEXT ,
                lname TEXT ,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL UNIQUE
            );
        """)

    #create another table called emergency_contact
cur.execute( ''' 
            CREATE TABLE IF NOT EXISTS emergency_contact 
            (
                id INTEGER  PRIMARY KEY AUTOINCREMENT,
                parents_tutor_name TEXT ,
                eEmail TEXT NOT NULL UNIQUE,
                ePhone TEXT NOT NULL UNIQUE
            );
    ''')

    # create another table called student_gpa
cur.execute( '''
            CREATE TABLE IF NOT EXISTS student_gpa 
            (
                id INTEGER NOT NULL,
                emergency_id NOT NULL,
                gpa REAl NOT NULL 
            );
    ''')

db_file.commit()
db_file.close()
