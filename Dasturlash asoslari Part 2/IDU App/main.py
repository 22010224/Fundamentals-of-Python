# Import necessary modules
import sqlite3

# Create a connection to the database
conn = sqlite3.connect('idu.db')

# Create a cursor object
cursor = conn.cursor()

# Define a function to display faculties
def display_faculties():
    cursor.execute('SELECT * FROM faculties')
    faculties = cursor.fetchall()
    print('List of Faculties:\n')
    for faculty in faculties:
        print(f'{faculty[0]}. {faculty[1]}')

# Define a function to display courses
def display_courses():
    cursor.execute('SELECT * FROM courses')
    courses = cursor.fetchall()
    print('List of Courses:\n')
    for course in courses:
        print(f'{course[0]}. {course[1]} ({course[2]} credits)')

# Define a function to display teachers
def display_teachers():
    cursor.execute('SELECT * FROM teachers')
    teachers = cursor.fetchall()
    print('List of Teachers:\n')
    for teacher in teachers:
        print(f'{teacher[0]}. {teacher[1]} ({teacher[2]})')

# Define a function to display students
def display_students():
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    print('List of Students:\n')
    for student in students:
        print(f'{student[0]}. {student[1]} ({student[2]})')

# Define a function to display tuition fees
def display_tuition_fees():
    cursor.execute('SELECT * FROM tuition_fees')
    tuition_fees = cursor.fetchone()
    print(f'Tuition Fees: {tuition_fees[0]}')

# Define a function to display campus information
def display_campus():
    cursor.execute('SELECT * FROM campus')
    campus = cursor.fetchone()
    print('Campus Information:\n')
    print(f'Location: {campus[0]}')
    print(f'Facilities: {campus[1]}')

# Define a function to display student union information
def display_student_union():
    cursor.execute('SELECT * FROM student_union')
    student_union = cursor.fetchone()
    print('Student Union Information:\n')
    print(f'Name: {student_union[0]}')
    print(f'President: {student_union[1]}')
    print(f'Vice President: {student_union[2]}')

# Define a function to add a new faculty
def add_faculty():
    name = input('Enter the name of the new faculty: ')
    cursor.execute(f"INSERT INTO faculties (name) VALUES ('{name}')")
    conn.commit()
    print(f'{name} has been added as a new faculty.\n')

# Define a function to add a new course
def add_course():
    name = input('Enter the name of the new course: ')
    credits = input('Enter the number of credits for the course: ')
    cursor.execute(f"INSERT INTO courses (name, credits) VALUES ('{name}', {credits})")
    conn.commit()
    print(f'{name} ({credits} credits) has been added as a new course.\n')

# Define a function to add a new teacher
def add_teacher():
    name = input('Enter the name of the new teacher: ')
    department = input('Enter the department of the new teacher: ')
    cursor.execute(f"INSERT INTO teachers (name, department) VALUES ('{name}', '{department}')")
    conn.commit()
    print(f'{name} ({department}) has been added as a new teacher.\n')

# Define a function to add a new student

