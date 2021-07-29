#1. How many students are there per major and major department?

import sqlite3

db_name = "student_major.db"

select_sql = """
    select d.department_name, m.major_name, count(s.id) as studentcount
    from student s
    inner join student_major sm on sm.student_id = s.id
    inner join major m on sm.major_id = m.id
    inner join department d on m.department_id = d.id
    group by d.department_name, m.major_name
    order by d.department_name asc
    """

with sqlite3.connect(db_name) as conn:
    cursor = conn.cursor()
    cursor.execute(select_sql)
    
    print("----------------------------------------------------------------------------------------------------------")
    print("Resultset showing department name, major name and number of students with major ordered by department name")
        
    # Displaying result set as statement see output1
    for row in cursor:
        print("Number of students in Department of " + row[0] + " with " + row[1] + " major is/are " + str(row[2]))

    # To display resultset without any customization see output 2
    # print("Department Name, Major Name, Number of Students")
    # for row in cursor:
    #     print(row)


# Output 1:
# (base) vineelabarre@Vineela-MacBook-Pro exercise % python question_two.py
# ----------------------------------------------------------------------------------------------------------
# Resultset showing department name, major name and number of students with major ordered by department name
# Number of students in Department of Engineering with Biocomputation major is/are 1
# Number of students in Department of Engineering with Computer Science major is/are 2
# Number of students in Department of Engineering with Electrical Engineering major is/are 1
# Number of students in Department of Language Arts with French major is/are 1
# Number of students in Department of Natural Sciences with Biology major is/are 1
# 
# Output 2:
# (base) vineelabarre@Vineela-MacBook-Pro exercise % python question_two.py
# ---------------------------------------------------------------------------------------------------------------
# Resultset showing department name, major name and number of students with that major ordered by department name
# Department Name, Major Name, Number of Students
# ('Engineering', 'Biocomputation', 1)
# ('Engineering', 'Computer Science', 2)
# ('Engineering', 'Electrical Engineering', 1)
# ('Language Arts', 'French', 1)
# ('Natural Sciences', 'Biology', 1)

