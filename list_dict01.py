# students = [
#     {"name": "Hermione Granger", "grade": 99},
#     {"name": "Ron Weasley", "grade": 78},
#     {"name": "Harry Potter", "grade": 82}

students: list[dict[str, any]]  = [
    {"name": "Matheus Fernandes", "grade": 10, "sex": "m"}, # dict 1
    {"name": "Ana Baggio", "grade": 9.9, "sex": "f"},       # dict 2
    {"name": "Felipe Cardozo", "grade": 7, "sex": "m"}      # dict 3
]

# print(students)
# print(students[0]) #Matheus
# print(students[1]) #Ana
# print(students[2]) #Felipe
# print(students[0]['grade'], students[0]['sex']) # mais de 2 keys dentro do list disctin

# Filter by Sex: Create a new list named male_students that contains the full dictionary of every student whose sex is "m".

male_students: list = []

for x in students:
    if x["sex"] == "m":
        male_students.append(x)
print(male_students)

# Find the Top Student: Iterate through the original students list to find the student with the highest grade and print their details.
top_student = students[0]
# Loop through the students to see if any have a higher grade.
for student in students:
    if student["grade"] > top_student["grade"]:
        top_student = student
print(f"Top grade: {top_student}")