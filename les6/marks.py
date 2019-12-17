students = {
'Ivanov': [2, 5, 3], 
'Petrov': [2, 5, 1], 
'Melnik': [3, 4, 5], 
'Zeleskaya': [5, 5, 5], 
'Martsin': [2, 1, 1], 
'Lavro': [4, 4, 4]
}

for key in students:
    students[key] = round(sum(students[key])/len(students[key]), 1)

print(students)

final_dict = dict([max(students.items(), key=lambda k_v: k_v[1])])
print(final_dict)

worst_student = dict([min(students.items(), key=lambda k_v: k_v[1])])
print(worst_student)