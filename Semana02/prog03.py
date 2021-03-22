# Ian Cardoso
# 11411EMT014

courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses[0])
print(courses[-1])
print(courses[2:])

courses.append("Art")
couses.insert(0, "Eng")

couses_2 = ['Art', 'Education']
#couses.insert(0, courses_2)
couses.extend(courses_2)

courses.remove('Math')
popped = courses.pop() #tira o ultimo e retorna
courses.reverse()
courses.sort() #alfabeticamente e ordem crescente

nums = [1,4,2,5,3]
nums.sort(reverse=True)

sorted_courses = sorted(courses)

print(min(nums))
print(max(nums))
print(sum(nums))

print('Math' in courses)

for item in couses:
	print(item)
for index, course in enumarate(courses, start=1):
	print(index, course)

print(courses)



## TUPLAS

course_str = '- '.join(courses)
new_list = course_str.split('- ')

print(course_str)



list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1


list_1[0] = 'Art'

print(list_1)
print(list_2)


tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1


tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)


cs_courses = {'History', 'Math', 'Physics', 'CompSci'}  #set nao tem ordem e remove valores duplicados
art_courses = {'History', 'Math', 'Design', 'Art'}

print(cs_courses.intersection(art_courses)
print(cs_courses.difference(art_courses)
print(cs_courses.union(art_courses)



empty_list = []
empty_list = list()


empty_tuple = ()
empty_tuple = tuple()


empty_set = {} #errado, cria um dicionario
empty_set = set()

