students = ['jon','hasan','husan','olim','botir']
marked_students ={}
while students:
    student = students.pop()
    mark = int(input(f"{student.title()} was marked with : "))
    print(f"{student.title()} has been marked!")
    marked_students[student] = mark

for stud, baho in marked_students.items():
    print(f"{student.title()} got {mark}")