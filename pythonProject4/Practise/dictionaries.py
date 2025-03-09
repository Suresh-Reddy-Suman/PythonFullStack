# employee_details = {
#     "name": "Suresh"
# }
#
# print(employee_details)
# print(employee_details['name'])
#
# employee_details['Location'] = 'Hyderabad'
#
# print(employee_details)
#
# employee_details['Location'] = 'Singapore'
# print(employee_details)
#
# for value in employee_details:
#     print(employee_details[value])

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    print(student)
    grade = ""
    if student_scores[student] > 90:
        grade = "Outstanding"
    elif student_scores[student] > 80:
        grade = "Exceeds Expectation"
    elif student_scores[student] > 70:
        grade = "Acceptable"
    elif student_scores[student] <70:
        grade = 'Fail'

    student_grades[student] = grade

print(student_grades)