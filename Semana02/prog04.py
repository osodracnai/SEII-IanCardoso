student = {'name': 'Ian', 'age': 23, 'courses': ['Math', 'CompSci']}

print(student['name'])
print(student.get('phone', 'Not found'))

student['phone']= '5555-555'
student.update({'name: 'Cardoso', 'age': 25, phone:'34543'})

del studen['age']
age = student.pop('age')
 

for key, value in student.items():
    print(key, value)
