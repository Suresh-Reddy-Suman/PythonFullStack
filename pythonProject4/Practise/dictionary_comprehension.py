# Create a dictionary with names from list with random score
import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
student_score = {student: random.randint(1, 99) for student in names}

print(student_score)

# Using the above dictionary print pass or fail based on the marks they got
passed_students = {student_name:score for (student_name, score) in student_score.items() if score > 60}

print(passed_students)