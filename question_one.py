# 1. List students by first name, last name, and major name sorted alphabetically by last name
#    have majors from the Engineering or Language Arts departments?

import sqlite3

db_name = "student_major.db"

# Retrieving data
select_sql = """
    select s.first_name, s.last_name, m.major_name
    from student s
    inner join student_major sm on sm.student_id = s.id
    inner join major m on sm.major_id = m.id
    inner join department d on m.department_id = d.id
    where d.id = 1 or d.id = 3
    order by last_name asc
    """

with sqlite3.connect(db_name) as conn:
    cursor = conn.cursor()
    try:
        cursor.execute(select_sql)  
        print("---------------------------------------------------------------------------")
        print("Resultset showing first name, last name, major name ordered by last name")
        print("First Name, Last Name, Major Name")
        for row in cursor:
            print(row)

    except sqlite3.Error as err:
            print(err)

# Output:
# (base) vineelabarre@Vineela-MacBook-Pro exercise % python question_one.py
# ---------------------------------------------------------------------------
# Resultset showing first name, last name, major name ordered by last name
# First Name,Last Name,Major Name
# ('Kelsey', 'Hightower', 'Electrical Engineering')
# ('Grace', 'Hopper', 'Computer Science')
# ('Geetha', 'Manjunath', 'Biocomputation')
# ('Geetha', 'Manjunath', 'Computer Science')
# ('John', 'Smith', 'French')

