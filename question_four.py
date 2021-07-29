# 1. How might you import students found in the dataset from `question_three.csv` into `student_major.db`
# (committing your changes to the database)?

import sqlite3
import csv

db_name = "student_major.db"

create_sql = """
        drop table if exists student_major_names;
        create table student_major_names (name text, major text);"""

# Reading question_three.csv file to add it to the database table
with open('question_three.csv','r') as csvdata, sqlite3.connect(db_name) as conn:
    cursor = conn.cursor()
    cursor.executescript(create_sql)
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(csvdata)
    to_db = [(row['Name'], row['Major(s)']) for row in dr]
    
    # Inserting data to student_major_names table
    cursor.executemany("INSERT INTO student_major_names (name, major) VALUES (?, ?);", to_db)
    conn.commit()

# Output:
# Creating a table student_major_names with two columns 'name' and 'major' in student_major.db
# database with below data from question_three.csv file
# 
# name	major
# Geetha Manjunath	Biocomputation, Computer Science
# Grace Hopper	Biology, Computer Science
# John Smith	French
# Kelsey Hightower	Electrical Engineering