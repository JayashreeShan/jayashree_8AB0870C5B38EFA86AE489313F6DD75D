class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa
def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students
students = [
    Student("Annamalai", "A001", 1992),
    Student("Baba", "B002", 2002),
    Student("Chandramuki", "C003", 2005),
    Student("Darbar", "D004", 2020),
]
sorted_students = sort_students(students)
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
