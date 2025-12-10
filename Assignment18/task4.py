def print_students(students):
    print("Student List:")
    for student in students:
        print(student)

student_input = input('Enter student names separated by commas: ')
student_names = [name.strip() for name in student_input.split(',')]
print_students(student_names)