# 1. How might you export a single dataset which includes students and their majors to a CSV file (named `question_three.csv`)?

import sqlite3
import csv

db_name = "student_major.db"

select_sql = """
    select s.first_name || ' ' || s.last_name as name,
           group_concat(m.major_name, ', ') as major
    from student s
    inner join student_major sm on sm.student_id = s.id
    inner join major m on sm.major_id = m.id
    group by s.first_name || ' ' || s.last_name
    order by s.first_name || ' ' || s.last_name asc
    """

with sqlite3.connect(db_name) as conn:
    csvWriter = csv.writer(open("question_three.csv", "w"))
    cursor = conn.cursor()
    cursor.execute(select_sql)
    result = cursor.fetchall()
    csvWriter.writerow(('Name', 'Major(s)'))

    for row in result:
        csvWriter.writerow(row)

# Output:
# question_three.csv file created with resultset shown below
# Name,Major(s)
# Geetha Manjunath,"Biocomputation, Computer Science"
# Grace Hopper,"Biology, Computer Science"
# John Smith,French
# Kelsey Hightower,Electrical Engineering
