# /c:/Users/Nancy Kumari/C tutorial/FUNCTION/STRUCTURE/AIPR/Assignment6/task1.py
# Simple Student class with user input

class Student:
    def __init__(self, name: str, roll: str, marks: list[float]):
        self.name = name
        self.roll = roll
        self.marks = marks
        self.average = None
        self.grade = None

    def calculate_average_and_grade(self):
        if not self.marks:
            self.average = 0.0
            self.grade = "N/A"
            return
        self.average = sum(self.marks) / len(self.marks)
        avg = self.average
        if avg >= 85:
            self.grade = "A"
        elif avg >= 70:
            self.grade = "B"
        elif avg >= 50:
            self.grade = "C"
        else:
            self.grade = "F"

    def display(self):
        print(f"Name : {self.name}")
        print(f"Roll : {self.roll}")
        print(f"Marks: {', '.join(f'{m:.1f}' for m in self.marks)}")
        print(f"Average: {self.average:.2f}")
        print(f"Grade: {self.grade}")


def read_marks(prompt="Enter marks separated by spaces: "):
    while True:
        s = input(prompt).strip()
        if not s:
            return []
        try:
            marks = [float(x) for x in s.split()]
            return marks
        except ValueError:
            print("Invalid input. Please enter numeric marks separated by spaces.")


def main():
    print("Create a student record")
    name = input("Student name: ").strip()
    roll = input("Roll number: ").strip()
    marks = read_marks()
    student = Student(name, roll, marks)
    student.calculate_average_and_grade()
    print("\nStudent information:")
    student.display()


if __name__ == "__main__":
    main()