# Define the student marks
marks = { 'A': 85, 'B': 67, 'C': 92, 'D': 74, 'E': 88 }

# Calculate the mean
mean_marks = sum(marks.values()) / len(marks)

# List students whose marks are above the mean
above_mean_students = [student for student, mark in marks.items() if mark > mean_marks]

# Output the results
print(f"Mean Marks: {mean_marks:.2f}")
print("Students above mean:", above_mean_students)