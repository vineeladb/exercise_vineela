# Add a new unique student record to the student table, notating and showing your work in the file created above.
# Creating answers.py to create student record and assigning existing major
# inserting new record to student table and adding French as their major

import sqlite3

db_name = "student_major.db"

insert_sql = """
    insert into student (id, first_name, last_name, dob) values (7, 'John', 'Smith', '1989-07-27');
    
    insert into student_major (id, student_id, major_id) values (6, 7, 9);
    """

with sqlite3.connect(db_name) as conn:
    cursor = conn.cursor()
    cursor.executescript(insert_sql)
    conn.commit()