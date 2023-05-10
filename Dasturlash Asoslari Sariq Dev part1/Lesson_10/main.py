car = {'model':'ferrari',
       'color':'red'}
print(car['model'])
print(car['color'])

student = {'name':'samandarbek',
           'age':18,
           't_year':2004}
print(f"{student['name'].title()}, {student['t_year']}-yilda tug\'ilgan, {student['age']} yosh")

print(student['name'].upper())
name = student.get('name')
print(name.title())

student['kurs'] = 4
print(student)


car = {}
car['model'] = 'Rolls Royce'
car['color'] = 'red'
car['year'] = 2023
print(car)
car['year'] = 2024
print(car)